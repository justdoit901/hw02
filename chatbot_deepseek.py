from volcengine.ark import ArkClient
from volcengine.core import VolcEngineConfig
import os
from dotenv import load_dotenv

load_dotenv()

def init_client():
    VolcEngineConfig.set_access_key(os.getenv("VOLC_ACCESS_KEY"))
    VolcEngineConfig.set_secret_key(os.getenv("VOLC_SECRET_KEY"))
    VolcEngineConfig.set_region(os.getenv("VOLC_REGION"))
    return ArkClient()

def chat_with_deepseek(client, question):
    try:
        response = client.chat.completions.create(
            model=os.getenv("VOLC_BOT_ID"),
            messages=[{"role": "user", "content": question}],
            temperature=0.7,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"调用失败：{str(e)}"

if __name__ == "__main__":
    client = init_client()
    print("✅ DeepSeek Chatbot 已启动！输入问题对话，输入 q 退出。")
    while True:
        user_input = input("你：")
        if user_input.lower() == "q":
            print("👋 对话结束！")
            break
        reply = chat_with_deepseek(client, user_input)
        print(f"DeepSeek：{reply}")
