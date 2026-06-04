from LLM.llm import llm
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_template(
    """
These OCR readings come from the same object.

OCR readings:
{ocr_history}

Rules:
- Merge repeated information.
- Preserve brand names.
- Preserve product names.
- Preserve numbers exactly.
- Do not explain.
- Do not summarize.
- Return only the corrected text.
"""
)



chain = prompt | llm 


def fix_ocr_text(data):
    result = chain.invoke(
        {
            "ocr_history" : "\n".join(data)
        }
    )

    return result.content.strip()
