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
        return result
    else:
        message = f"API request failed with status code {response.status_code}: {response.text}"
        return message
    
result = GPT_api_call("""Here is the text. Create two short questions and one Long question from it.
                      Also create three fill in the branks from it and only give result in response.                     
                      
                       \"Once a crow was looking for something to eat. Suddenly he saw a piece of cheese.
                       He lifted the piece in his beak. He flew to a tree nearby.A fox was also in search of food.
                       While wandering he came under that tree. He saw the crow and his piece of cheese. His mouth watered.
                       He wanted to have it. He was very cunning. He hit upon a plan to trick the crow.He said to the crow.
                      "You are a fine bird. Your wings are very pretty. Your voice must be very sweet. Would you not sing me a song?\"""")
content = result['choices'][0]['message']['content']
# print(type(content))
print(content)
# print(result[0]['message']['content'])