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
    
    all_data = requests.get(url)
    
    return all_data.text