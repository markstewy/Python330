"""
Scripts to run to set up our database
"""

from models import db, User, People
# from passlib.hash import pbkdf2_sha256


# Create the database tables for our model
db.connect()
db.drop_tables([User, People])
db.create_tables([User, People])

People(name="Nick Cage", city="San Clemente").save()
People(name="Emma Watson", city="Hogsmead").save()
People(name="Dwane Johnson", city="Rockhester").save()
People(name="Tom Hanks", city="Next Door").save()
People(name="Elijah Wood", city="Shire").save()
People(name="Carrie Underwood", city="Alderon").save()
People(name="Kelly Slater", city="Miami").save()