import urllib.request,json
from .models_sources import Source
from .models_article import Article
from datetime import datetime


api_key = None
base_sources_url = None
base_articles_url = None

def configure_request(app):
    global api_key, base_articles_url, base_sources_url
    api_key = app.config['NEWS_API_KEY']
    print(api_key)
    base_sources_url = app.config['NEWS_SOURCES_API_BASE_URL']
    base_articles_url = app.config['NEWS_ARTICLES_API_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_sources_url.format(category,api_key)
    print(get_source_url)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)
        print(get_source_response)
        sources_lists = None

        if get_source_response['sources']:
            sources_lists_list = get_source_response['sources']
            sources_lists = process_sources(sources_lists_list)

    return sources_lists


def process_sources(sources_list):
    '''
    Function  that processes the source results and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain movie details
    Returns :
        sources_list: A list of source objects
    '''
    sources_lists = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id, name, description, url, category, language, country)
        sources_lists.append(source_object)

    return sources_lists




def get_articles():
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = base_articles_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_lists = None

        if get_articles_response['articles']:
            articles_lists_list = get_articles_response['articles']
            articles_lists = process_articles(articles_lists_list)

    return articles_lists

def process_articles(articles_list):
    '''
    Function  that processes the articles results and transform them to a list of Objects
    Args:
        articles_list: A list of dictionaries that contain articles details
    Returns :
        articles: A list of articles objects
    '''
    articles = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        name = articles_item.get('name')
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('conent')

        article_object = Article(id, name, author, title, description, url, urlToImage, publishedAt, content)
        articles.append(article_object)

    return articles_lists