import os

class Config:

    NEWS_API_KEY = '135ffda36d8343da8d3a44adf0505e08'
    SECRET_KEY = os.environ.get('SECRET_KEY')

    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?category={}&apiKey={}'
    NEWS_ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    
    pass


class DevConfig(Config):
   
    DEBUG = True

config_options = {
    'development':DevConfig,
    'productions':ProdConfig
}