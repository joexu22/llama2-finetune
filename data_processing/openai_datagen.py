import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

questions = [
    "What are MSE and RMSE?",
    "Explain DBSCAN algorithm?",
    "What are dummy variables?"
]

for question in questions:
    prompt = f"Explain {question} in a simple and relatable way."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    print(f"{question}\n{response.choices[0].text.strip()}\n")
