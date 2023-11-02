import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "As an expert OpenAI API Developer, create a list of 5 apps that can use OPENAI api"}])
print(completion.choices[0].message.content)