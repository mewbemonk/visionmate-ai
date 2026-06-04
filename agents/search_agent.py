from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from LLM.llm import llm



search = DuckDuckGoSearchRun()


prompt = ChatPromptTemplate.from_template(
    """
Question:
{question}

Search Results:
{search_results}

Rules:

- Use ONLY the detected information.
- Do NOT use your own knowledge.
- Do NOT guess.
- If answer is not explicitly present in detected information,
  return EXACTLY:

SEARCH_REQUIRED
"""
)


chain = prompt | llm 





def search_agent(context,question):

    query = f"{context} {question}"

    search_results = search.invoke(query)

    print(search_results)

    res = chain.invoke({
        "context" : context,
        "question" : question,
        "search_results" : search_results
    })


    return res.content.strip()

