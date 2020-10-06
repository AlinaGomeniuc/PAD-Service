from mongoengine import connect
from flask import Flask


def configure_app():
    connect("user-db")
    app = Flask(__name__)
    app.config['MONGODB_DB'] = 'user-db'
    return app


app = configure_app()
