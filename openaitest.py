from Database.config import apikey
import openai

openai.api_key = apikey
prompt = input("Enter work.")
command = []
command.append({'role': 'system', 'content': prompt})

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=command,
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
# print(response)
print(response["choices"][0]["message"]["content"])