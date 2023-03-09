# @app.route("/books", endpoint="lst_books")
from flask import render_template

from app.authers import auth_blueprint

# <a href={{url_for("deleteBook" , id=book.id)}} class="buy">Delete Bppk</a>


""" 

def get_books():
    books = Books.query.all()
    return render_template("lst_books.html", books=books)


def bookDetail(id):
    print(id)
    book = Books.query.get(id)
    return render_template("bookDetails.html", book=book)
 """
