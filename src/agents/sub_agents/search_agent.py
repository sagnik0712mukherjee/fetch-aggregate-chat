from crewai import Agent

def search_based_on_user_query(user_query):

    searching_agent = Agent(
        role = "Intelligent Web Search Agent",
        goal = f"Search the best information available based on user's query: {user_query}as per information available on the internet.",
        backstory = "You are a master at performing real time internet search to expand the capabilities of the LLM which may not be up to date with recent data.",
        verbose = True
    )

    return searching_agent