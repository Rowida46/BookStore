from .models import Book
# @app.route("/books", endpoint="lst_books")
from flask import render_template

# <a href={{url_for("deleteBook" , id=book.id)}} class="buy">Delete Bppk</a>


def home():
    return render_template("index.html")


def get_books():
    books = Book.query.all()
    return render_template("lst_books.html", books=books)


def bookDetail(id):
    print(id)
    book = Book.query.get(id)
    return render_template("bookDetails.html", book=book)
