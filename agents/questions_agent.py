from langchain_core.prompts import ChatPromptTemplate
from LLM.llm import llm

prompt = ChatPromptTemplate.from_template(
"""
You are helping a visually impaired user.

Detected Information:
{context}

User Question:
{question}

Rules:
- Answer only using the detected information.
- Keep answer short.
- If the answer is not present in the detected information,
  return ONLY:

SEARCH_REQUIRED
"""
)


chain = prompt | llm


def questions(context,question):

    res = chain.invoke({

        "context" : context,
        "question" : question
    })

    return res.content.strip()