from crewai import Crew
from src.agents.sub_agents.chunking_agent import chunk_based_on_obtained_data
from src.agents.sub_agents.scraping_agent import scrape_based_on_user_query
from src.agents.sub_agents.search_agent import search_based_on_user_query
from src.tasks.chunker_task import get_chunking_task
from src.tasks.scraping_task import get_scrape_task
from src.tasks.searching_task import get_search_task

def build_crew(user_query, top_k):

    search_agent = search_based_on_user_query(user_query)
    scraping_agent = scrape_based_on_user_query(user_query)
    chunker_agent = chunk_based_on_obtained_data()

    search_task = get_search_task(user_query, top_k)
    scrape_task = get_scrape_task(user_query)
    chunker_task = get_chunking_task()

    crew = Crew(
        agents=[search_agent, scraping_agent, chunker_agent],
        tasks=[search_task, scrape_task, chunker_task],
        verbose=True
    )

    return crew