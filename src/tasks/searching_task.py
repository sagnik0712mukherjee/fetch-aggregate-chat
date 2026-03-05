from crewai import Task
from src.agents.sub_agents.search_agent import search_based_on_user_query
from config.settings import task_data_path
from src.tools.search_tool import web_search

def get_search_task(user_query, top_k):

    search_agent = search_based_on_user_query(user_query)

    searching_task = Task(
        description=f"""
            Conduct a thorough search about the user query: {user_query}.
            Make sure you find top interesting and relevant information
            as per the current year (2026).
        """,
        expected_output=f"""
            An array of strings with the top {top_k} results from the search.
        """,
        agent=search_agent,
        markdown=True,
        output_file=f"{task_data_path}/search.md",
        tools=[web_search]
    )

    return searching_task