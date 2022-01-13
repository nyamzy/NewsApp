from flask import render_template
from app import app
from app.request import get_sources, get_articles

@app.route('/')
def index():
    """
    Index view function for getting the news sources
    """
    general_sources = get_sources('general')
    tech_sources = get_sources('technology')
    business_sourcess = get_sources('business')

    title = 'Home - Get all the news you want'

    return render_template('index.html', title = title, general = general_sources, technology = tech_sources, business = business_sourcess)

@app.route('/source/<id>')
def article(id):
    """
    Article view function for displaying news articles
    """
    article = get_articles(id)
    title = f'{id} stories'

    return render_template('article.html', title = title, article = article)


