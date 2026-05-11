import os
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import INSTRUCTION_TEMPLATES

load_dotenv()

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates
templates = Jinja2Templates(directory="templates")

def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")
    return genai.Client()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/api/templates")
async def get_templates():
    return INSTRUCTION_TEMPLATES

class EvaluateRequest(BaseModel):
    input_kb: str

@app.post("/api/evaluate")
async def evaluate(data: EvaluateRequest):
    input_kb = data.input_kb
    if not input_kb:
        return JSONResponse({"error": "Missing required fields"}, status_code=400)

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            # Mock mode if no valid API key
            score = 60 # Force fail to test mock reconstruction
            reasoning = "MOCK MODE: KB is poor."
            improved_kb = "MOCK RECONSTRUCTED KB: This is the improved mock KB that meets all standards."
            score = 100
            return {
                "score": score,
                "reasoning": reasoning + " -> Reconstructed by AI.",
                "improved_kb": improved_kb
            }

        client = get_client()

        # Step 1: Evaluate KB
        eval_prompt = f"""
You are an expert Data Cleaner and Content Auditor. Your task is to evaluate the following Input Knowledge Base.
Check for the following issues:
1. Formatting: Does it have excessive blank spaces, blank lines, or unwanted junk characters?
2. Relevancy & Coherence: Is the content coherent, logically structured, and highly relevant to its own stated topic? Does it contain off-topic garbage or noise?

Return a quality score from 0 to 100, where 100 means the KB is perfectly formatted, clean, coherent, and highly relevant.
Provide a brief reasoning for your score.

Input Knowledge Base:
{input_kb}

Output your response strictly as a JSON object with two keys: "score" (a number) and "reasoning" (a string). Do not use markdown blocks.
"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=eval_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        result_text = response.text.strip()
        if result_text.startswith("```json"):
            result_text = result_text.replace("```json", "").replace("```", "").strip()
        elif result_text.startswith("```"):
            result_text = result_text.replace("```", "").strip()

        eval_result = json.loads(result_text)
        score = eval_result.get("score", 0)
        reasoning = eval_result.get("reasoning", "")

        improved_kb = None
        if score < 75:
            reconstruct_prompt = f"""
You are an expert Knowledge Base Editor. The following Input Knowledge Base scored poorly on formatting, cleanliness, or coherence.
Your task is to clean up and restructure the text.
Fix the following issues without changing the core factual intent:
- Remove excessive blank spaces, blank lines, and junk characters.
- Remove unwanted, irrelevant, or noisy off-topic data.
- Ensure consistent, readable, and clean structuring.

Reasoning for poor score:
{reasoning}

Original Input Knowledge Base:
{input_kb}

Return ONLY the fully cleaned and formatted Knowledge Base without any markdown wrapping or additional conversational text.
"""
            reconstruct_response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=reconstruct_prompt,
            )
            improved_kb = reconstruct_response.text.strip()
            score = 100
            reasoning = reasoning + " -> Reconstructed by AI to meet standards."

        return {
            "score": score,
            "reasoning": reasoning,
            "improved_kb": improved_kb
        }

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

class GenerateRequest(BaseModel):
    input_kb: str
    instruction_template: Optional[str] = None
    instruction_type: Optional[str] = "Sales"
    extra_instructions: Optional[str] = ""

@app.post("/api/generate")
async def generate(data: GenerateRequest):
    input_kb = data.input_kb
    instruction_template = data.instruction_template
    extra_instructions = data.extra_instructions.strip() if data.extra_instructions else ""
    
    if not instruction_template:
        instruction_type = data.instruction_type
        instruction_template = INSTRUCTION_TEMPLATES.get(instruction_type, INSTRUCTION_TEMPLATES.get("Sales", ""))

    if not input_kb:
        return JSONResponse({"error": "Missing required fields"}, status_code=400)

    if extra_instructions:
        instruction_template += f"\n\n--- ADDITIONAL INSTRUCTIONS ---\n{extra_instructions}\n"

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            final_instructions = f"MOCK AGENT INSTRUCTIONS:\n1. Mock behavior.\n(Evaluated and reconstructed by Mock AI)"
            return {
                "final_instructions": final_instructions,
                "auditor_score": 50,
                "auditor_reasoning": "MOCK MODE: Initial instructions were poor.",
                "was_refined": True
            }

        client = get_client()
        instr_prompt = f"""
You are an expert AI agent configuration generator. Based on the provided Input Knowledge Base, generate the final AI agent instructions using the provided Instruction Template.

Instruction Template:
{instruction_template}

Input Knowledge Base:
{input_kb}

Return only the final generated instructions.
"""
        instr_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=instr_prompt,
        )
        initial_instructions = instr_response.text.strip()

        # Agent Instruction Evaluator
        eval_instr_prompt = f"""
You are an AI auditor. Evaluate the following generated agent instructions against the Instruction Template.
Determine if the generated instructions perfectly follow the structure, tone, and requirements of the Instruction Template.
Return a relevance score from 0 to 100, where 100 means perfect match.
Provide a brief reasoning.

Instruction Template:
{instruction_template}

Generated Instructions:
{initial_instructions}

Output your response strictly as a JSON object with two keys: "score" (a number) and "reasoning" (a string).
"""
        eval_resp = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=eval_instr_prompt,
            config=types.GenerateContentConfig(response_mime_type="application/json"),
        )
        
        eval_text = eval_resp.text.strip()
        if eval_text.startswith("```json"):
            eval_text = eval_text.replace("```json", "").replace("```", "").strip()
        elif eval_text.startswith("```"):
            eval_text = eval_text.replace("```", "").strip()

        eval_result = json.loads(eval_text)
        instr_score = eval_result.get("score", 0)
        instr_reasoning = eval_result.get("reasoning", "")

        final_instructions = initial_instructions

        was_refined = False
        if instr_score < 75:
            was_refined = True
            refine_prompt = f"""
You are an expert AI configuration refiner. The previously generated instructions were evaluated as not up to standard.
Rewrite them perfectly to match the Instruction Template.

Auditor Reasoning:
{instr_reasoning}

Instruction Template:
{instruction_template}

Original Flawed Instructions:
{initial_instructions}

Return ONLY the fully refined agent instructions.
"""
            refine_response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=refine_prompt,
            )
            final_instructions = refine_response.text.strip()

        return {
            "final_instructions": final_instructions,
            "auditor_score": instr_score,
            "auditor_reasoning": instr_reasoning,
            "was_refined": was_refined
        }
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

class QaRequest(BaseModel):
    input_kb: str

@app.post("/api/generate_qa")
async def generate_qa(data: QaRequest):
    input_kb = data.input_kb
    
    if not input_kb:
        return JSONResponse({"error": "Missing input_kb"}, status_code=400)

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            return {
                "qa_list": [
                    {"question": "Mock Question?", "answer": "Mock Answer.", "type_of_question": "Mock Type"}
                ]
            }

        client = get_client()
        qa_prompt = f"""
You are an expert customer support analyst. Based on the following Knowledge Base, generate a list of atleast 25 a customer might ask that can be trivial as well as advanced questions . 
For each question, provide the answer based strictly on the KB, and categorize the 'type_of_question' (e.g., Pricing, Feature, Support, General).

Input Knowledge Base:
{input_kb}

Output your response strictly as a JSON array of objects, where each object has the keys: "question", "answer", and "type_of_question". Do not use markdown blocks.
"""
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=qa_prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        result_text = response.text.strip()
        if result_text.startswith("```json"):
            result_text = result_text.replace("```json", "").replace("```", "").strip()
        elif result_text.startswith("```"):
            result_text = result_text.replace("```", "").strip()

        qa_list = json.loads(result_text)
        return {"qa_list": qa_list}

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=5000, reload=True)
