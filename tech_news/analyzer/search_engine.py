from pymongo import MongoClient
from tech_news.database import db
import re
from datetime import datetime


# Requisito 7
def search_by_title(title):
    searched_news = []
    with MongoClient():
        for new in db.news.find({"title": re.compile(title, re.IGNORECASE)},
                                {"_id": 0, "title": 1, "url": 1}):
            new_title = new["title"]
            new_url = new["url"]
            new_tuple = tuple((new_title, new_url))
            searched_news.append(new_tuple)
        return searched_news


# Requisito 8
def search_by_date(date):
    searched_news = []
    try:
        dateObject = datetime.strptime(date, "%Y-%m-%d")
        print(dateObject)
    except ValueError:
        raise ValueError("Data inválida")
    d = datetime.strptime(date, "%Y-%m-%d")
    formated_date = d.strftime('%d/%m/%Y')
    with MongoClient():
        for new in db.news.find({"timestamp": formated_date},
                                {"_id": 0, "title": 1, "url": 1}):
            new_title = new["title"]
            new_url = new["url"]
            new_tuple = tuple((new_title, new_url))
            searched_news.append(new_tuple)
        return searched_news


# Requisito 9
def search_by_category(category):
    searched_news = []
    with MongoClient():
        for new in db.news.find({"category": re.compile(category,
                                re.IGNORECASE)},
                                {"_id": 0, "title": 1, "url": 1}):
            new_title = new["title"]
            new_url = new["url"]
            new_tuple = tuple((new_title, new_url))
            searched_news.append(new_tuple)
        return searched_news
