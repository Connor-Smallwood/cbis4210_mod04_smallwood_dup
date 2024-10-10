from sqlalchemy import Enum
from . import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key, auto-incremented
    title = db.Column(db.String(100), nullable=False)  # Title of the book, max length of 100 characters
    genre = db.Column(db.String(50), nullable=False)  # Genre, max length of 50 characters
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Price as a decimal (e.g., 9.99)

    # Age group defined as an Enum to restrict values to predefined categories
    age_group = db.Column(Enum('0-2', '3-5', '6-8', '9-12', 'teens', 'adults', name='age_groups'), nullable=False)

    description = db.Column(db.Text, nullable=False)  # Longer description field
    image = db.Column(db.String(100))  # Optional image field, can be null


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key, auto-incremented
    first_name = db.Column(db.String(50), nullable=False)  # First name, max length of 50 characters
    last_name = db.Column(db.String(50), nullable=False)  # Last name, max length of 50 characters
    description = db.Column(db.Text)  # Optional longer description about the author
