from mongoengine import connect
from flask import Flask


def configure_app():
    connect(db="user-db",
            host='mongodb://mongo_db')
    app = Flask(__name__)
    app.config['MONGODB_DB'] = 'user-db'
    return app


app = configure_app()
