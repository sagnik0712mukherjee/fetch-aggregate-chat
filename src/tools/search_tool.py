from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool

@tool("DuckDuckGoSearch")
def web_search(query):
    """
    The function is used to perform real time web-search on the internet.

    Args:
        query (str): the user Query for search
        top_k (int | default = 3): the number of results to be retrieved.
    
    Return:
        Search results in array of strings.
    """

    results = DuckDuckGoSearchRun().run(query)
    
    return results