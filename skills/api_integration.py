import openai
import requests

def call_openai_api(prompt):
    return openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7
    )

def call_rest_api(url, data, headers=None):
    response = requests.post(url, json=data, headers=headers)
    return response.json()
