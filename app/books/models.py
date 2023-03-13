from .. models import db
from app.models import db
from datetime import datetime


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    rate = db.Column(db.Integer, default=4, nullable=True)
    image = db.Column(db.String(300))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated = db.Column(db.DateTime, onupdate=datetime.utcnow)
    author_id = db.Column(
        db.Integer, db.ForeignKey('author.id'), nullable=True)

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_all_Books(cls):
        return cls.query.all()

    @classmethod
    def get_specific_book(cls, id):
        return cls.query.get(id)

    def delete_book(self):
        db.session.delete(self)
        db.session.commit()
        return True

    @classmethod
    def create_newBook(cls, book_new_obj):
        # newBook = cls(**book_new_obj)
        db.session.add(book_new_obj)
        db.session.commit()
        return book_new_obj

    @classmethod
    def delete_Book(cls, book_new_obj):
        # newBook = cls(**book_new_obj)
        db.session.delete(book_new_obj)
        db.session.commit()
        return True

    def update_book(self, updated_data):
        """  
         db.session.add(self)
         db.session.commit()
         return True

        """
        pass
