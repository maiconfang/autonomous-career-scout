from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
    max_tokens=300
)

print(
    response.choices[0].message.content
)