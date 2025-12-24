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
prompt_token_count = req.usage_metadata.prompt_token_count
candidates_token_count = req.usage_metadata.candidates_token_count


def main():
    print("User prompt:", content)
    print("Response tokens:", candidates_token_count)
    print("Prompt tokens:", prompt_token_count)
    print("Response:", resp)


if __name__ == "__main__":
    main()
