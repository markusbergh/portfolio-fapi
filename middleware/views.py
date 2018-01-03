from flask import jsonify, abort, request

# Helpers
from middleware import app, client

# Models
from models import Article, Project


@app.route('/v1/content/front_page', methods=['GET'])
def get_frontpage():
    entry = {}
    request = client.entries({'content_type': 'frontPage', 'include': 3})
    item = request.items[0]

    entry = {
        'title': item.title,
        'introduction': item.introduction,
        'about': {
            'image': item.about.image.url(),
            'image_text': item.about.image_text,
            'description': item.about.description,
            'skills': item.about.skills,
        },
        'contact': {
            'text': item.contact_label,
            'email': item.contact_email,
        },
        'footer': {
            'copyright': item.footer.copyright,
            'technology': item.footer.technology,
            'content_provider': {
                'text': item.footer.content_provider,
                'image': item.footer.content_provider_logotype.url()
            },
            'love': item.footer.love,
            'items': []
        },
    }

    for index, item in enumerate(item.footer.items):
        entry['footer']['items'].append({
            'id': item.sys['id'],
            'items': [],
        })

        for subitem in item.items:
            entry['footer']['items'][index]['items'].append({
                'id': subitem.sys['id'],
                'text': subitem.text,
                'link': subitem.link,
            })

    return jsonify(entry)


@app.route('/v1/projects/<string:project_id>', methods=['GET'])
def get_project(project_id):
    project = None
    list = client.entries({'content_type': 'project', 'sys.id': project_id})

    for item in list:
        project = Project(id=item.id)
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
    list = {}
    use_short = False

    if request.args.get('slug'):
        list = client.entries({
            'content_type': 'project',
            'fields.slug': request.args.get('slug'),
        })
    else:
        list = client.entries({'content_type': 'project'})
        use_short = True

    for item in list:
        project = Project(id=item.id)
        project.cover = item.cover.url()
        project.description = item.description
        project.screens = item.screens
        project.short_description = item.short_description
        project.slug = item.slug
        project.thumbnail = item.thumbnail.url()
        project.title = item.title
        project.year = item.year

        projects.append(project)

    if len(projects) == 0:
        abort(404)

    return jsonify([project.serialize(use_short=use_short) for project in projects])


@app.route('/v1/articles/<string:article_id>', methods=['GET'])
def get_article(article_id):
    article = None
    list = client.entries({'content_type': 'article', 'sys.id': article_id})

    for item in list:
        article = Article(id=item.id)
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
    list = {}
    use_short = False

    if request.args.get('slug'):
        list = client.entries({
            'content_type': 'article',
            'fields.slug': request.args.get('slug'),
        })
    else:
        use_short = True
        list = client.entries({'content_type': 'article'})

    for item in list:
        article = Article(id=item.id)
        article.body = item.body
        article.category = item.category
        article.cover = item.cover.url()
        article.date = item.date
        article.title = item.title
        article.slug = item.slug

        articles.append(article)

    if len(articles) == 0:
        abort(404)

    return jsonify([article.serialize(use_short=use_short) for article in articles])
