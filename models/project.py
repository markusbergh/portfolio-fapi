# project.py

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
