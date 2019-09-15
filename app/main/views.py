from flask import render_template, request, redirect, url_for
from ..models_article import Article
from ..models_sources import Source
from ..requests import get_articles, get_sources
from . import main

@main.route('/')
def index():
    """
    This  it's gone turn index.html page and it content
    """
    isoko = get_sources('general')

    head = "ALLOVER THE WORLD NEWS"
    return render_template('index.html', title = head, isoko = isoko)

@main.route('/isoko/<id>')
def news_article(id):
    """
    This is gone to returns articles details
    """
    articles = get_articles(id)
    return render_template('news_article.html', articles = articles)