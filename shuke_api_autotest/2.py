from openai import OpenAI

client = OpenAI(
    base_url="https://api.deepseek.com/",
    api_key="sk-c78ea179b6a94b21b80bf397b4abff37"
)

completion = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
                "role": "user",
                "content": "请帮我用 HTML 生成一个五子棋游戏，所有代码都保存在一个 HTML 中。"
        }
    ]
)

print(completion.choices[0].message.content)