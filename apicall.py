import requests
import json

open_ai_api_key = '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'
url = 'https://api.openai.com/v1/chat/completions'
def GPT_api_call(incoming_text):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {open_ai_api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': f'{incoming_text}'}],
        'temperature': 0.7
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        result = response.json() #["Content"] we can get only contents of the response
        print(result)
        return result
    else:
        message = f"API request failed with status code {response.status_code}: {response.text}"
        print(message)
        return message