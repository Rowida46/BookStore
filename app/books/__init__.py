from flask import Blueprint


books_blueprint = Blueprint('books', __name__, url_prefix='/book')
from app.books import views
