from flask import render_template, request, redirect, url_for
from ..models_article import Article
from ..models_sources import Source
from ..requests import get_articles, get_sources
from . import main

@main.route('/')
def news_source():
    """
    This  it's gone turn news_source.html page and it content
    """
    isoko = get_sources('general')

    head = "ALLOVER THE WORLD NEWS"
    return render_template('news_source.html', title = head, sources = isoko)

@main.route('/isoko/<articles_id>')
def news_article(articles_id):
    """
    This is gone to returns articles details
    """
    articles = get_articles()
    return render_template('news_article.html', articles = articles)