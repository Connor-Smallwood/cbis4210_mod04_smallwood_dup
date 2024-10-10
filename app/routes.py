from flask import Blueprint, render_template, request
from .models import Book, Author

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/books')
def books():
    # Fetch all books from the database
    genre = request.args.get('genre')
    price = request.args.get('price')
    age_group = request.args.get('age_group')

    # You can add filter logic here if required (e.g., filter by genre, price, etc.)
    all_books = Book.query.all()

    return render_template('books.html', books=all_books)

@main.route('/electronics')
def electronics():
    # Simulated electronics data (you will replace this with your own logic)
    electronics = [
        {"name": "Headphones", "description": "Noise-canceling headphones.", "price": 99.99, "image": "#"},
        {"name": "Laptop", "description": "High-performance laptop.", "price": 599.99, "image": "#"},
    ]

    return render_template('electronics.html', electronics=electronics)

@main.route('/authors')
def authors():
    # Fetch all authors from the database
    all_authors = Author.query.all()

    return render_template('authors.html', authors=all_authors)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/help')
def help_page():
    return render_template('help.html')
