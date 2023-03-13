from flask_restful import Resource, Api, marshal_with, abort
from app.books.models import Book
from app.books.api.serializers import Bookerilizer
from app.books.api.parser import bookparser
from app.models import db

from app.books.models import Book

class lstBook(Resource):
    @marshal_with(Bookerilizer)
    def get(self):
        books = Book.get_all_Books()
        return books

    @marshal_with(Bookerilizer)
    def post(self):
        Book = bookparser.parse_args()
        newBook = Book(**Book)
        db.session.add(newBook)
        db.session.commit()
        return newBook, 201


class PostGetSpecificAndUpdateAndDelete(Resource):
    @marshal_with(Bookerilizer)
    def get(self, id):
        book = Book.get_specific_book(id)
        if book:
            return book, 200

        return abort(404, message="book not found")

    @marshal_with(Bookerilizer)
    def put(self, id):
        book = Book.query.get(id)
        if book:
            post_args = bookparser.parse_args()
            book.update_post(post_args)
            return book, 200

        return abort(205, message="book not found")

    def delete(self, id):
        book = Book.get_specific_book(id)
        if book:
            book.delete_book()
            return {"deleted": "book Deleted"}
        return 'page not found ',404 