import os
import requests

from dotenv import load_dotenv
from ayarlar import BUSINESS_CONTEXT


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY bulunamadı. .env dosyanı kontrol et.")


def ask_ai(user_message):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "qwen/qwen3.8-27b",
        "messages": [
            {
                "role": "system",
                "content": f"""
Sen Ahenk adlı kahve markasının AI asistanısın.

Ahenk hakkında temel bilgiler:
{BUSINESS_CONTEXT}

Kullanıcıya sıcak, samimi ve yardımcı bir şekilde cevap ver.
Bilmediğin bir konuda bilgi uydurma.
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(
            f"Groq API hatası: {response.status_code}\n{response.text}"
        )

    result = response.json()

    return result["choices"][0]["message"]["content"]


if __name__ == "__main__":
    print("AI servisi çalışmaya başladı.")
    cevap = ask_ai("Merhaba, sen kimsin?")
    print("AI cevabı:")
    print(cevap)