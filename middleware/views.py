# views.py

from flask import jsonify, abort

# Helpers
from middleware import app, client

# Models
from models import Article

@app.route('/v1/articles/<string:article_id>', methods=['GET'])
def get_article(article_id):
    article = None

    for item in client.entries({'content_type': 'article', 'sys.id': article_id}):
        article = Article(id = item.id)
        article.date = item.date
        article.cover = item.cover.url()
        article.title = item.title
        article.body = item.body

    if article is None:
        abort(404)

    return jsonify(article.serialize())

@app.route('/v1/articles', methods=['GET'])
def get_articles():
    articles = []

    for item in client.entries({'content_type': 'article'}):
        article = Article(id = item.id)
        article.date = item.date
        article.cover = item.cover.url()
        article.title = item.title
        article.body = item.body

        articles.append(article)

    if len(articles) == 0:
        abort(404)

    return jsonify([article.serialize() for article in articles])
