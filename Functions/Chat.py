from openai import OpenAI

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)

def chat(query):
    completion = client.chat.completions.create(
      model="mistralai/mistral-7b-instruct:free",
      messages=[
        {
          "role": "system",
          "content": query,
        },
      ],
    )

    return completion.choices[0].message.content
    

# while True:
#     query = input("Enter query:")
#     print(chat(query))