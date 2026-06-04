from langchain_core.prompts import ChatPromptTemplate
from LLM.llm import llm


prompt = ChatPromptTemplate.from_template(

"""
You are a routing agent.

Text:
{text}

Rules:

If text is short:
return read

If text is long:
return summarize

If text needs explanation:
return explain

Return ONLY one word.

read
explain
summarize
"""

)


chain = prompt | llm



def decide_task(text):
    res =  chain.invoke({
        "text" : text
    })

    return res.content.strip()