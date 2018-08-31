class Config:
    
    NEWS_API_BASE_URL='https://newsapi.org/v2/sources?&category={}&apiKey={}'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

#we have 3 classes one is the parent and all the others from it the dev config enables us to debug        
