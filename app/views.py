from flask import render_template
from app import app
from .request import get_news


@app.route('/news/<int:news_id>')
def news(news_id):
    return render_template('news.html',id = news_id)  
@app.route('/')
def index():
    #getting categories
    category_news = get_news('sports')
    print(category_news)
    title = 'great news here'
    return render_template('index.html',title = title, category_news = category_news)