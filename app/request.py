from app import app
import urllib.request, json

from app.article_test import Article
from .models import source, article

Source = source.Source
Article = article.Article

#Getting the api key
api_key = app.config['NEWS_API_KEY']

#Getting the news source url
base_url = app.config['SOURCE_BASE_URL']

#Getting the news articles url
base_url2 = app.config['NEWS_ARTICLES_URL']

def get_sources(category):

    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_sources(source_results_list)

    return source_results

def process_sources(source_list):
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        if name:
            source_object = Source(id, name, description)

            source_results.append(source_object)

    return source_results


def get_articles(id):

    get_articles_url = base_url2.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        article_details_data = url.read()
        article_details_response = json.loads(article_details_data)

        articles_results = None

        if article_details_response['articles']:
           articles_result_list = article_details_response['articles']
           articles_results = process_articles(articles_result_list)

    return articles_results


def process_articles(article_list):

    articles_results = []

    for article_item in article_list:
        id = article_item.get('id')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        time = article_item.get('publishedAt')

        if image:
            article_object = Article(id, title, description, url, image, time)
            articles_results.append(article_object)

    return articles_results