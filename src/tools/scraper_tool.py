import requests
from crewai.tools import tool


@tool("WebScraper")
def scrape_url(url):
    """
    The function is used to scrape a URL and return the HTML text data from the web-page.

    Args:
        url (str): the Url of the web-page to be scraped

    Return:
        Textual html data
    """

    try:
        all_data = requests.get(url, timeout=10)
        all_data.raise_for_status()
        return all_data.text
    except Exception as e:
        return f"[Scraper Error] Failed to scrape {url}. Error: {str(e)}"
