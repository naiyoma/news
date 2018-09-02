from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_articles, get_news
from ..models import News,Articles

@main.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)  
@main.route('/')
def index():
    #getting categories
    category_news = get_news('sports')
    technology = get_news('technology')
    business = get_news('business')
    print(category_news)
    title = 'great news here'
    return render_template('index.html',title = title, category_news = category_news, technology = technology, business = business)

@main.route('/news/<id>')
def articles(id):
    articles = get_articles(id)

    return render_template('news.html',articles=articles)   

# 1.we import render template function from flask that will take my html templates as arguments and then load them
# 2.creationg main decorators that will define function index
#3.route number one has a news function and i mapped the movie_id so that we can get a response in my news.html
#4.