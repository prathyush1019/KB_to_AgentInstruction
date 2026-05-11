import os
import json
import requests

def call_gemini(prompt, format_json=False):
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise Exception("GEMINI_API_KEY environment variable not set.")

    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    generation_config = {}

    if format_json:
        generation_config["response_mime_type"] = "application/json"

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": generation_config
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        result = response.json()

        return result["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.RequestException as e:
        raise Exception(f"Gemini request failed: {str(e)}")

    except Exception as e:
        raise Exception(f"Gemini parsing failed: {str(e)}")