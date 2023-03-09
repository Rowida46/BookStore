from .. models import db
from app.models import db


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    books = db.relationship('Book', backref='author', lazy=True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def authers(cls):
        return cls.query.all()
