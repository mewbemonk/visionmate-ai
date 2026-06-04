import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


llm = ChatOpenAI(
    model="openai/gpt-oss-120b:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("MEWBEMONK"),
    temperature=0.2
)