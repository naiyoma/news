
import os
class Config:
    
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?&category={}&apiKey={}'
    ARTICLES_API_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}    

#we have 3 classes one is the parent and all the others from it the dev config enables us to debug        
