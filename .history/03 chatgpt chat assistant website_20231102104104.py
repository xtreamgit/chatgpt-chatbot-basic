import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a python developer that specializes in scrapping content from websites to create datasets that can be used to train models."}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Web Scrapper Tool")

demo.launch(share=True)