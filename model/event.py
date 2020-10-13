from mongoengine import EmbeddedDocument, StringField


class Event(EmbeddedDocument):
    type = StringField(max_length=50, required=True)
    status = StringField(max_length=50, required=True)
    timestamp = StringField()
