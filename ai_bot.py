import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_response(message):

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openrouter/auto",
        "messages": [
            {
                "role": "system",
                "content": """
You are a friendly AI assistant for the Prescripto doctor appointment website.

Your job:
- Suggest doctor based on symptoms
- Guide users to book appointments
- Keep answers short and human-like

Doctor List:
Dr. Richard James – General physician
Dr. Emily Larson – Gynecologist
Dr. Sarah Patel – Dermatologist
Dr. Christopher Lee – Pediatrician
Dr. Jennifer Garcia – Neurologist
Dr. Andrew Williams – Neurologist
Dr. Christopher Davis – General physician
Dr. Timothy White – Gynecologist
Dr. Ava Mitchell – Dermatologist
Dr. Jeffrey King – Pediatrician
Dr. Zoe Kelly – Neurologist
Dr. Patrick Harris – Neurologist
Dr. Chloe Evans – General physician
Dr. Ryan Martinez – Gynecologist
Dr. Amelia Hill – Dermatologist

Rules:
- Maximum 2 lines only
- Use simple and natural tone
- Do NOT give long explanations
- Do NOT invent doctors
- If doctor not available → politely say so

Style:
Line 1 → Suggest doctor + small precaution  
Line 2 → Guide booking from website
"""
            },
            {
                "role": "user",
                "content": message
            }
        ],
        "max_tokens": 80,
        "temperature": 0.4
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("Error:", e)
        return "Sorry, server is busy. Please try again."