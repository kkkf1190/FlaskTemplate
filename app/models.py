from mongoengine import Document,StringField,EmailField,connect

connect('test')

class user:
    username = StringField(required=True)
    usermail = EmailField()
    password = StringField(required=True)