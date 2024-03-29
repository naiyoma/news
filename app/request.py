
import urllib.request,json
from .models import News
from .models import Articles

# News = news.News
# Articles = articles.Articles
#Getting api key
api_key = '6fea05c04bb243cd8d0fe4a6fb98dbc7'

#Getting the news base url
# base_url = None 
base_url='https://newsapi.org/v2/sources?&category={}&apiKey={}'

#Getting the articles base url
base2_url ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'

# def configure_request(app):
#     global api_key,base_url,base2_url
#     api_key = app.config['NEWS_API_KEY']
#     base_url = app.config['NEWS_API_BASE_URL']
#     base2_url = app.config['ARTICLES_API_BASE_URL']
    


def get_news(category):
    get_news_url = base_url.format(category, api_key)
    print(get_news_url)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response =json.loads(get_news_data)
        
        news_result = None

        if get_news_response["sources"]:
            news_sources_list = get_news_response["sources"]
            news_result = process_news(news_sources_list)

    return news_result

def process_news(news_list):
    
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

def get_articles(id):
    get_articles_url = base2_url.format(id,api_key)
    print(get_articles_url)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response =json.loads(get_articles_data)
        print(get_articles_response)
        
        articles_result = None

        if get_articles_response["articles"]:
            articles_sources_list = get_articles_response["articles"]
            articles_result = process_articles(articles_sources_list)

    return articles_result


def process_articles(articles_list):
    
    articles_results=[]
    for news_item in articles_list:
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')
        if urlToImage:
            aricles_object = Articles(author,title,description,url,urlToImage,publishedAt)
            articles_results.append(aricles_object)

    return articles_results  

def search_news(news_name):
    search_news_url =  'https://api.themoviedb.org/3/search/movie?api_key={}&query={}'.format(api_key,news_name)
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']:
            search_news_list = search_news_response['results']
            # search_news_results = process_results(search_news_list)   

    return search_news_results 

# 1.folder where all API  calls  and request will be made
#2.impoerting the urllib.request is connecting me to the API URL
#3. we then access the configurations and the pass in the base urls and the key and the base url
#4.the first function which is the get_news function takes in category as a argument and the call the.format method which will replace {} as place hlders this will generate our get news url which we will use to make the request
# the read method reads the news data ,with which is the context manager sends request to the base url
#conver json response to a python dictionary using load we then return the news list(results)

#process_news 
# 1 created a function that will take in the news list 
# an empty news list which will store the news objects of our news is then created
# we loop through each element in the news_list and then pass in the id to access the data
# we then check if the movie item has a url and then create an news object which will be appended to our empty list
