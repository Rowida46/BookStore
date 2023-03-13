
# project confiration options ->

import os
# developemt , production


class Config:
    SECRET_KEY = os.urandom(32)

    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///BookStore.db'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:dana46@localhost:5432/bookstore"


class ProductionConfig(Config):
    DEBUG = False
    # postgresql:://username:password@localhost:portnumber/dbname
    # SQLALCHEMY_DATABASE_URI = "postgresql://pythonmenair2:iti@localhost:5432/menia_flask"
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:dana46@localhost:5432/bookstoredep"


projectConfig = {
    'dev': DevelopmentConfig,
    'prd': ProductionConfig
}
