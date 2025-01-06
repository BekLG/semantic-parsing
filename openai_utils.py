import os

from openai import OpenAI



def openai_generate(messages: list, model: str = 'gpt-4', **generation_params):
    client = OpenAI()

    completion = client.chat.completions.create(
        messages=messages,
        model=model,
        **generation_params
    )
    return completion#.choices[0].message.content