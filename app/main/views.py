from flask import render_template, request, redirect, url_for
from ..models News_article, News_source
from ..requests import get_article, get_source
from . import main

@main.route('/')
def index():
    """
    This  it's gone turn index.html page and it content
    """
    isoko = get_source()

    head = "ALLOVER THE WORLD NEWS"
    return render_template('index.html', title = head, sources = isoko)

@main.route('/news_article/<articles_id>')
def news_article(articles_id):
    """
    This is gone to returns articles details
    """
    articles = get_articles()
    return render_template('news_article.html', articles = articles)