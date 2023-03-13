from ..books.BookForm import BookForm
from .models import Book
from flask import render_template, redirect, request, jsonify
# <a href={{url_for("deleteBook" , id=book.id)}} class="buy">Delete Bppk</a>
# from app.books import books_blueprint

from app.books import books_blueprint

from app.authers.models import Author


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


@books_blueprint.route("delete/<id>", endpoint="delete_book")
def bookDetail(id):
    print(id)
    print("---------------")

    book = Book.query.get(id)
    Book.delete_Book(book)
    print("---------------")
    return redirect("get_books")


@books_blueprint.route('/createBook', methods=['POST', 'GET'], endpoint="create_new_book")
def addNewPost():
    form = BookForm()
    authers = Author.query.all()
    print("--------------------", authers)
    if request.method == 'GET':
        return render_template("create.html", form=form, authers=authers)
    if request.method == 'POST':
        newBook = Book()
        newBook.title = request.form['title']
        newBook.description = request.form['description']
        newBook.image = request.form['image']
        newBook.rate = request.form['rate']
        # newBook.author_id = request.form['auth']

        Book.create_newBook(newBook)
        return redirect('lst_books')


@books_blueprint.route('/update/<int:id>/', methods=('GET', 'POST'), endpoint="update_book")
def update(id):
    form = Book.query.get_or_404(id)
    authers = Author.query.all()

    if request.method == 'GET':
        return render_template('create.html', form=form, authers=authers)
    if request.method == 'POST':
        title = request.form['title']
        # title = request.form.get('title')
        if title is None:
            return jsonify({'error': 'Title is missing'}), 400

        editBook = Book(**request.form)
        Book.create_newBook(editBook)
        return redirect('get_books')
