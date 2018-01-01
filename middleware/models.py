class Article():
    """This class represents an article."""

    id = ''
    body = ''
    category = ''
    cover = ''
    date = ''
    title = ''

    def __init__(self, id):
        self.id = id

    def serialize(self):
        return {
            'body': self.body,
            'category': self.category,
            'cover': self.cover,
            'date': self.date,
            'title': self.title,
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
    screens = ''

    def __init__(self, id):
        self.id = id

    def get_screen_url(self, screen):
        return screen.url()

    def serialize(self, use_short=False):
        if use_short is True:
            return {
                'short_description': self.short_description,
                'thumbnail': self.thumbnail,
                'title': self.title,
                'year': self.year
            }

        return {
            'cover': self.cover,
            'description': self.description,
            'screens': map(self.get_screen_url, self.screens),
            'title': self.title,
            'year': self.year,
        }
