from flask import Flask
from flask import jsonify, abort, make_response

import contentful

from models.article import Article

app = Flask(__name__)
app.config.from_object('config')

# Credentials for Contentful
spaceId = app.config['SPACE_ID']
accessToken = app.config['ACCESS_TOKEN']

# Set up client
client = contentful.Client(spaceId, accessToken)

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

if __name__ == '__main__':
    app.run()
