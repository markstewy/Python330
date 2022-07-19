import os
from peewee import Model, CharField, IntegerField
from playhouse.db_url import connect

# if there is an env variable called DATABASE_URL connect to that, if not connect
# to 'sqlite:///my_database.db' ad the default
db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))

class User(Model):
    name = CharField(max_length=255, unique=True)
    city = CharField(max_length=255, unique=True)
    email = CharField(max_length=255, unique=True)
    password = CharField(max_length=255, unique=True)

    class Meta:
        database = db

class People(Model):
    name = CharField(max_length=255, unique=True)
    city = CharField(max_length=255, unique=True)

    class Meta:
        database = db
