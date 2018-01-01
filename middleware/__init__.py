from flask import Flask

import contentful

app = Flask(__name__)

app.config.from_object('config')

# Credentials for Contentful
spaceId = app.config['SPACE_ID']
accessToken = app.config['ACCESS_TOKEN']

# Set up client
client = contentful.Client(spaceId, accessToken)

if __name__ == '__main__':
    app.run()
