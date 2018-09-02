
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

# 1.i have created 3 classes the 1st is the parent which contains all my configurations
# 2.the 2nd and 3rd configurations inherit configurations from our parent the devconfig helps in debugging       
