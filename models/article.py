# article.py

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
