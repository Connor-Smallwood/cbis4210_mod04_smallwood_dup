from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    age_group = db.Column(db.String(20), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
