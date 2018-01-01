# models.py

class Article():
    """This class represents an article."""

    id = ''
    title = ''
    body = ''
    cover = ''
    date = ''
    category = ''

    def __init__(self, id):
        self.id = id

    def serialize(self):
        return {
            'date': self.date,
            'title': self.title,
            'body': self.body,
            'cover': self.cover,
        }

class Project():
    """This class represents a project."""

    id = ''
    cover = ''
    description = ''
    short_description = ''
    slug = ''
    thumbnail = ''
    title = ''
    year = ''

    def __init__(self, id):
        self.id = id

    def serialize(self):
        return {
            'cover': self.cover,
            'description': self.description,
            'title': self.title,
            'year': self.year,
        }
