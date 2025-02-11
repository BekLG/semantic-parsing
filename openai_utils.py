import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print(os.getenv('OPENAI_API_KEY'))

def openai_generate(messages: list, model: str = 'gpt-4', **generation_params):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))  # Fixed initialization

    completion = client.chat.completions.create(
        messages=messages,
        model=model,
        **generation_params
    )
    return completion