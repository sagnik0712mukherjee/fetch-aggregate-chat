from crewai import Task
from src.agents.sub_agents.scraping_agent import scrape_based_on_user_query

from config.settings import task_data_path
from src.tools.scraper_tool import scrape_url

def get_scrape_task(user_query):

    scraping_agent = scrape_based_on_user_query(user_query)

    scraping_task = Task(
        description=f"""
            Conduct a thorough web-scraping task about the user query: {user_query}.
            Make sure you find at-most 1 best suited URL with the relevant information
            as per the current year (2026). Extract the HTML data of the web-page.
        """,
        expected_output="""
            The HTML Text extracted from the scraped web-page. Mention the parent URL from which the scraping has been done.
        """,
        agent=scraping_agent,
        markdown=True,
        output_file=f"{task_data_path}/scrape.md",
        tools=[scrape_url]
    )

    return scraping_task