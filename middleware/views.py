# views.py

from flask import jsonify, abort

# Helpers
from middleware import app, client

# Models
from models import Article, Project

@app.route('/v1/projects/<string:project_id>', methods=['GET'])
def get_project(project_id):
    project = None

    for item in client.entries({'content_type': 'project', 'sys.id': project_id}):
        project = Project(id = item.id)
        project.cover = item.cover.url()
        project.description = item.description
        project.screens = item.screens
        project.title = item.title
        project.year = item.year

    if project is None:
        abort(404)

    return jsonify(project.serialize())

@app.route('/v1/projects', methods=['GET'])
def get_projects():
    projects = []

    for item in client.entries({'content_type': 'project'}):
        project = Project(id = item.id)
        project.cover = item.cover.url()
        project.description = item.description
        project.screens = item.screens
        project.title = item.title
        project.year = item.year

        projects.append(project)

    if len(projects) == 0:
        abort(404)

    return jsonify([project.serialize() for project in projects])

@app.route('/v1/articles/<string:article_id>', methods=['GET'])
def get_article(article_id):
    article = None

    for item in client.entries({'content_type': 'article', 'sys.id': article_id}):
        article = Article(id = item.id)
        article.body = item.body
        article.category = item.category
        article.cover = item.cover.url()
        article.date = item.date
        article.title = item.title

    if article is None:
        abort(404)

    return jsonify(article.serialize())

@app.route('/v1/articles', methods=['GET'])
def get_articles():
    articles = []

    for item in client.entries({'content_type': 'article'}):
        article = Article(id = item.id)
        article.body = item.body
        article.category = item.category
        article.cover = item.cover.url()
        article.date = item.date
        article.title = item.title

        articles.append(article)

    if len(articles) == 0:
        abort(404)

    return jsonify([article.serialize() for article in articles])
