from tech_news.database import create_news
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
    selector = Selector(html_content)
    url = selector.css('link[rel~="canonical"]::attr(href)').get()
    title = selector.css('div.entry-header-inner.cs-bg-dark > h1::text').get()
    timestamp = selector.css('.meta-date::text').get()
    writer = selector.css('.url.fn.n::text').get()
    reading_time = selector.css('.meta-reading-time::text').get().split()
    sum = selector.css('div.entry-content > p:nth-of-type(1) *::text').getall()
    category = selector.css('.label::text').get()
    dict_new = {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time[0]),
        "summary": "".join(sum).strip(),
        "category": category,
    }

    return dict_new


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    news = []
    count = 0

    while count < amount:
        content = fetch(url)
        links = scrape_updates(content)

        for new in links:
            if count == amount:
                break
            new_content = fetch(new)
            new_data = scrape_news(new_content)
            news.append(new_data)
            count += 1

        url = scrape_next_page_link(content)

    create_news(news)

    return news
