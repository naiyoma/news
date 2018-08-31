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
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)

    return news_results

def get_new(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None
        if new_details_response:
            id = new_details_response.get('id')
            name = new_details_response.get('name')
            description = new_details_response.get('description')
            url = new_details_response.get('url')
            category= new_details_response.get('category')
            language = new_details_response.get('language')
            country = new_details_response.get('country')
        new_object=News(id,name,description,url,category,language,country)

    return new_object        
