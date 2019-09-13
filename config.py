import os

class Config:
    '''
    General configuration parent class
    '''

    NEWS_API_KEY = '135ffda36d8343da8d3a44adf0505e08'
    SECRET_KEY = 'ALEXIE'

    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    NEWS_ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig
}