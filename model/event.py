from mongoengine import EmbeddedDocument, DateTimeField, StringField, ReferenceField
# from model.user import User


class Event(EmbeddedDocument):
    type = StringField(max_length=50, required=True)
    status = StringField(max_length=50, required=True)
    timestamp = StringField()
