from crewai import Agent

def scrape_based_on_user_query(user_query):

    scraping_agent = Agent(
        role = "Intelligent Web Scraper Agent",
        goal = f"Scrape the best website (ONLY 1) possible to get information based on user's query: {user_query}. Make sure website is simplistic with single page and only textual, tabular and image data and does not comply to piracy. Scrape information from the latest information available on the internet as per current year (2026).",
        backstory = "Users have been querying intensively about AI and its growth. With several blogs available, you are a master of picking the best information providing web-page for the user's use case.",
        verbose = True
    )

    return scraping_agent