import os

from dotenv import load_dotenv

from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():

    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
    # llm = OpenAI(temperature=0.9, openai_api_key=OPENAI_API_KEY)
    result = llm.invoke("Give me 5 topics for interesting YouTube videos about Python")
    print(result)

if __name__ == "__main__":
    main()