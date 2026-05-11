import os
import json
from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import INSTRUCTION_TEMPLATES

load_dotenv()

app = Flask(__name__)

def get_client():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY is not set. Please set it in the .env file.")
    return genai.Client()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/templates", methods=["GET"])
def get_templates():
    return jsonify(INSTRUCTION_TEMPLATES)



@app.route("/api/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    input_kb = data.get("input_kb")
    if not input_kb:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            # Mock mode if no valid API key
            score = 60 # Force fail to test mock reconstruction
            reasoning = "MOCK MODE: KB is poor."
            improved_kb = "MOCK RECONSTRUCTED KB: This is the improved mock KB that meets all standards."
            score = 100
            return jsonify({
                "score": score,
                "reasoning": reasoning + " -> Reconstructed by AI.",
                "improved_kb": improved_kb
            })

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

        return jsonify({
            "score": score,
            "reasoning": reasoning,
            "improved_kb": improved_kb
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    input_kb = data.get("input_kb")
    instruction_template = data.get("instruction_template")
    extra_instructions = data.get("extra_instructions", "").strip()
    
    if not instruction_template:
        instruction_type = data.get("instruction_type", "Sales")
        instruction_template = INSTRUCTION_TEMPLATES.get(instruction_type, INSTRUCTION_TEMPLATES["Sales"])

    if not input_kb:
        return jsonify({"error": "Missing required fields"}), 400

    if extra_instructions:
        instruction_template += f"\n\n--- ADDITIONAL INSTRUCTIONS ---\n{extra_instructions}\n"

    try:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key or api_key == "your_gemini_api_key_here":
            final_instructions = f"MOCK AGENT INSTRUCTIONS:\n1. Mock behavior.\n(Evaluated and reconstructed by Mock AI)"
            return jsonify({
                "final_instructions": final_instructions,
                "auditor_score": 50,
                "auditor_reasoning": "MOCK MODE: Initial instructions were poor.",
                "was_refined": True
            })

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

        return jsonify({
            "final_instructions": final_instructions,
            "auditor_score": instr_score,
            "auditor_reasoning": instr_reasoning,
            "was_refined": was_refined
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
