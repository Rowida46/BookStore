
from flask import Flask
from flask_migrate import Migrate

from app.models import db

from app.config import projectConfig as appConfig  # dic -> of dev&prd mood
from app.books.models import Book

from app.authers.models import Author

# import configration -> spesify wither u r in production in dev mood ->.


def create_app(config_name):
    app = Flask(__name__)

    current_config = appConfig[config_name]  # class
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    # search in this class about class variable with this name
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config

    app.config.from_object(current_config)  # read configration
    db.init_app(app)  # initalize app
    # add migration
    migrate = Migrate(app, db)

    # route of books
    from app.books.views import home, get_books, bookDetail
    app.add_url_rule('/', view_func=home)
    app.add_url_rule('/lst_books', view_func=get_books)
    app.add_url_rule('/oneBook/<id>', view_func=bookDetail)

    from app.books.errors import error_view
    # app.error("/notFound", view_func=error_view)
    app.register_error_handler(404, error_view)
    return app
