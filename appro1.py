from requests import get
from bs4 import BeautifulSoup

import bs4

import Algorithmia

client = Algorithmia.client("simWYZZvrLoNQu0jhCwHWQvuz1J1")

def get_links():
    """Gets links from URL"""
    input = "https://twitter.com/rashtrapatibhvn/status/1166247247027113985"
    if input.startswith("http") or input.startswith("https"):
        algo = client.algo('web/GetLinks/0.1.5')
        links = algo.pipe(input).result
        return links
    else:
        print("Please enter a properly formed URL")

def get_content():
    """Get text content from URL."""
    data = get_links()
    algo = client.algo("util/Url2Text/0.1.4")
    # Limit content extracted to only blog articles
    content = [{"url": link, "content": algo.pipe(
        link).result} for link in data if link.startswith("https://twitter.com/rashtrapatibhvn/status/1166247247027113985")]
    return content
