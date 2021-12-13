from flask import render_template
from app import app
from app.request import get_sources

@app.route('/')
def index():
    news_sources = get_sources()

    title = 'Home - Get all the news you want'

    return render_template('index.html', title = title, source = news_sources)
    
