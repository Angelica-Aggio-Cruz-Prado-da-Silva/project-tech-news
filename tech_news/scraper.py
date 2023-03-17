import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, wait: int = 3):
    try:
        for _ in range(15):
            response = requests.get(url, timeout=wait)
            response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    links = []
    for article in selector.css('.entry-header'):
        link = article.css('h2 a::attr(href)').get()
        links.append(link)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    element = 'a.next.page-numbers::attr(href)'
    next_page = selector.css(element).get()

    return next_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
