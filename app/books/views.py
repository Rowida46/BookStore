from .models import Book
# @app.route("/books", endpoint="lst_books")
from flask import render_template

# <a href={{url_for("deleteBook" , id=book.id)}} class="buy">Delete Bppk</a>
# from app.books import books_blueprint

from app.books import books_blueprint


@books_blueprint.route("/", endpoint="home")
def home():
    return render_template("index.html")


@books_blueprint.route("/lst_books", endpoint="get_books")
def get_books():
    books = Book.query.all()
    return render_template("lst_books.html", books=books)


@books_blueprint.route("oneBook/<id>", endpoint="bookDetail")
def bookDetail(id):
    print(id)
    book = Book.query.get(id)
    return render_template("bookDetails.html", book=book)
