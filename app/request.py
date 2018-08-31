from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api key
api_key = app.config['NEWS_API_KEY']

#Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"] 
def get_news(category):
    get_news_url = base_url.format(category, api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response =json.loads(get_news_data)
        
        news_result = None

        if get_news_response["sources"]:
            news_sources_list = get_news_response["sources"]
            news_result = process_sources(news_sources_list)

    return news_result

def process_sources(news_list):
    
    news_results=[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        if url:
            news_object = News(id,name,description,url,category)
            news_results.append(news_object)

    return news_results    