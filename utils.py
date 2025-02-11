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



def df_to_str(df):
    # Step 1: Apply filtering logic
    filtered_df = df[
        (df["id"] > 3) &  # Assuming 'id' is a numeric identifier
        (df["avg_lifespan_change_percent"] > 17)  # Filtering based on lifespan change
    ]

    # Step 2: Select and rename relevant columns
    selected_columns = [
        "id", "compound_name", "species", "strain", "dosage",
        "age_at_initiation", "treatment_duration", "avg_lifespan_change_percent",
        "avg_lifespan_significance", "max_lifespan_change_percent",
        "max_lifespan_significance", "gender_new", "weight_change_percent",
        "weight_change_significance", "ITP", "pubmed_id", "notes"
    ]
    filtered_df = filtered_df[selected_columns]

    # Step 3: Round numeric columns to four decimal places
    numeric_cols = [
        "avg_lifespan_change_percent", "max_lifespan_change_percent", "weight_change_percent"
    ]
    filtered_df[numeric_cols] = filtered_df[numeric_cols].round(4)

    # Step 4: Convert the DataFrame to a Markdown-style table
    return filtered_df.to_markdown(index=False, tablefmt="pipe")


