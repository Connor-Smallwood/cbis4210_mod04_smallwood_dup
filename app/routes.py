from flask import Blueprint, render_template, redirect, url_for, request
from .models import Book, Author
from . import db

# Define the main blueprint
main = Blueprint('main', __name__)


# Home page
@main.route('/')
def index():
    return render_template('index.html')


# ==============================
# Books Routes
# ==============================

# Display all books
@main.route('/books')
def books():
    genre = request.args.get('genre')
    price = request.args.get('price')
    age_group = request.args.get('age_group')

    # Fetch all books from the database
    all_books = Book.query.all()

    return render_template('books.html', books=all_books)


# CREATE a new book
@main.route('/create-book', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        genre = request.form['genre']
        price = request.form['price']
        age_group = request.form['age_group']
        description = request.form['description']
        image = request.form['image']  # Handle the image URL or path

        # Save the new book to the database (assuming you have a Book model)
        new_book = Book(title=title, genre=genre, price=price, age_group=age_group, description=description,
                        image=image)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('main.books'))

    return render_template('create_book.html')


# UPDATE an existing book
@main.route('/update-book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book = Book.query.get_or_404(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.genre = request.form['genre']
        book.price = request.form['price']
        book.age_group = request.form['age_group']
        book.description = request.form['description']
        book.image = request.form['image']  # Update the image URL or path

        db.session.commit()
        return redirect(url_for('main.books'))

    return render_template('update_book.html', book=book)


# DELETE a book
@main.route('/delete-book/<int:id>')
def delete_book(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('main.books'))


# ==============================
# Authors Routes
# ==============================

# Display all authors
@main.route('/authors')
def authors():
    # Fetch all authors from the database
    all_authors = Author.query.all()

    return render_template('authors.html', authors=all_authors)


# CREATE a new author
@main.route('/create-author', methods=['GET', 'POST'])
def create_author():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        description = request.form['description']
        image = request.form['image']  # Handle the image URL or path

        # Save the new author to the database (assuming you have an Author model)
        new_author = Author(first_name=first_name, last_name=last_name, description=description, image=image)
        db.session.add(new_author)
        db.session.commit()

        return redirect(url_for('main.authors'))

    return render_template('create_author.html')


# UPDATE an existing author
@main.route('/update-author/<int:id>', methods=['GET', 'POST'])
def update_author(id):
    author = Author.query.get_or_404(id)
    if request.method == 'POST':
        author.first_name = request.form['first_name']
        author.last_name = request.form['last_name']
        author.description = request.form['description']
        author.image = request.form['image']  # Update the image URL or path

        db.session.commit()
        return redirect(url_for('main.authors'))

    return render_template('update_author.html', author=author)


# DELETE an author
@main.route('/delete-author/<int:id>')
def delete_author(id):
    author = Author.query.get_or_404(id)
    db.session.delete(author)
    db.session.commit()
    return redirect(url_for('main.authors'))


# ==============================
# Electronics Route (From Previous)
# ==============================

@main.route('/electronics')
def electronics():
    # Simulated electronics data (you will replace this with your own logic)
    electronics = [
        {"name": "Headphones", "description": "Noise-canceling headphones.", "price": 99.99, "image": "#"},
        {"name": "Laptop", "description": "High-performance laptop.", "price": 599.99, "image": "#"},
    ]

    return render_template('electronics.html', electronics=electronics)


# ==============================
# About and Help Pages (From Previous)
# ==============================

# About page
@main.route('/about')
def about():
    return render_template('about.html')


# Help & FAQ page
@main.route('/help')
def help_page():
    return render_template('help.html')
