import requests

import pandas as pd
import json


def webservice_generate(prompt: str, **generation_params):
    url = "http://127.0.0.1:5000/v1/completions"
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "prompt": prompt,
    }

    for key, value in generation_params.items():
        data[key] = value

    response = requests.post(url, headers=headers, json=data)
    return response.json()


def postprocess_response(response) -> dict:
    dict_start_idx = response.find('{')
    if dict_start_idx != -1:
        response = response[dict_start_idx:]
    generation_result = json.loads(response)
    return generation_result