from mongoengine import Document, StringField, ListField, EmbeddedDocumentField
from model.event import Event


class User(Document):
    name = StringField(max_length=50, required=True)
    surname = StringField(max_length=50, required=True)
    status = StringField(max_length=50, required=True)
    worked_hours = StringField()
    events = ListField(EmbeddedDocumentField(Event))
