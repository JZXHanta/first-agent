import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

model = "gemini-2.5-flash"
content = "Why is Boot.dev dush a great place to learn backend development?"

req = client.models.generate_content(model=model, contents=content)
resp = req.text


def main():
    print(resp)


if __name__ == "__main__":
    main()
