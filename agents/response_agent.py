from LLM.llm import llm
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template(
    """
You are helping a visually impaired person.

Text:
{text}

Rules:
- Explain in one short sentence.
- Keep response under 20 words.
- Be simple.
"""
)




chain = prompt | llm


def response(text):
    res = chain.invoke({
        "text" : text
    })

    return res.content.strip()