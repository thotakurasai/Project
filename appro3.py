from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

import bs4

import Algorithmia

client = Algorithmia.client("simWYZZvrLoNQu0jhCwHWQvuz1J1")


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


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
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

