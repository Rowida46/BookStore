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
