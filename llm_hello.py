import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://coding.dashscope.aliyuncs.com/v1",
)

response = client.chat.completions.create(
    model="qwen3.6-plus",
    max_tokens=200,
    messages=[
        {
            "role": "user",
            "content": "用一句话解释什么是RAG，面向前端工程师。"
        }
    ]
)

print(response.choices[0].message.content)