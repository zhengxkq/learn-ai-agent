import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://coding.dashscope.aliyuncs.com/v1",
)


print("AI：", end="", flush=True)

stream = client.chat.completions.create(
    model="qwen3.6-plus",
    max_tokens=300,
    stream=True,
    messages=[
        {"role": "user", "content": "用一句话解释什么是 RAG,面向前端工程师。"}
    ]
)


for chunk in stream:
    delta = chunk.choices[0].delta.content
    if delta:
        print(delta, end="", flush=True)

print()