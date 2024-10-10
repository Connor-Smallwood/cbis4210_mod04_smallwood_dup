from flask import Blueprint, render_template, request
from .models import Book, Author

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/books')
def books():
    # Simulate filters (You can replace this with actual dynamic filters using the database)
    genre = request.args.get('genre')
    price = request.args.get('price')
    age = request.args.get('age')

    # Simulated book data (later you will replace this with actual database queries)
    books = [
        {"title": "Book One", "description": "A great read.", "price": 9.99, "image": "#"},
        {"title": "Book Two", "description": "Another great book.", "price": 12.99, "image": "#"},
    ]

    return render_template('books.html', books=books)


@main.route('/electronics')
def electronics():
    # Simulated electronics data
    electronics = [
        {"name": "Headphones", "description": "Noise-canceling.", "price": 99.99, "image": "#"},
        {"name": "Laptop", "description": "Great for work.", "price": 599.99, "image": "#"},
    ]

    return render_template('electronics.html', electronics=electronics)


@main.route('/authors')
def authors():
    # Simulated filters for authors
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    # Simulated author data (later you will replace this with actual database queries)
    authors = [
        {"first_name": "John", "last_name": "Doe", "description": "Author of many bestsellers."},
        {"first_name": "Jane", "last_name": "Smith", "description": "A famous fiction author."},
    ]

    return render_template('authors.html', authors=authors)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/help')
def help_page():
    return render_template('help.html')
