from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenRouter client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# 🔹 AI response only
def get_response(message):
    print("User:", message)

    response = client.chat.completions.create(
        model="openrouter/auto",
        messages=[
            {
                "role": "system",
                "content": """
            You are an AI assistant for the Prescripto doctor appointment website.

            Your job:
            - Suggest doctors based on symptoms
              doctors list:
                Dr. Richard James – General physician
Dr. Emily Larson – Gynecologist
Dr. Sarah Patel – Dermatologist
Dr. Christopher Lee – Pediatricians
Dr. Jennifer Garcia – Neurologist
Dr. Andrew Williams – Neurologist
Dr. Christopher Davis – General physician
Dr. Timothy White – Gynecologist
Dr. Ava Mitchell – Dermatologist
Dr. Jeffrey King – Pediatricians
Dr. Zoe Kelly – Neurologist
Dr. Patrick Harris – Neurologist
Dr. Chloe Evans – General physician
Dr. Ryan Martinez – Gynecologist
Dr. Amelia Hill – Dermatologist
            - if not available in list according to symptoms than apologize to user
            - if available than Guide users to book appointments

            STRICT RULES:
            - Answer in MAXIMUM 2 lines only
            - Use simple and short sentences
            - Do NOT explain too much
            - Sounds like natural and Human
            - Do NOT give long advice
            - Always be direct

            Style:
             Suggest Initial needed precautions
             then doctor suggestion
             and then how to book


            """
            },
            {
                "role": "user",
                "content": message
            }
        ],
        max_tokens=150
    )

    reply = response.choices[0].message.content

    print("Bot:", reply)

    return reply