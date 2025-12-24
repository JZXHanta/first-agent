import os

from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

model = "gemini-2.5-flash"
content = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

req = client.models.generate_content(model=model, contents=content)
resp = req.text


def main():
    print(content)
    print(resp)


if __name__ == "__main__":
    main()
