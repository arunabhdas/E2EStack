import os

from dotenv import load_dotenv

from langchain.llms import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    llm = OpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY)
    result = llm.predict("Give me 5 topics for interesting YouTube videos about Python")
    print(result)

if __name__ == "__main__":
    main()