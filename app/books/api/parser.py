from flask_restful import reqparse

bookparser = reqparse.RequestParser()

bookparser.add_argument(
    'title', type=str, help='Title is required', required=True)
bookparser.add_argument('description', type=str)
bookparser.add_argument(
    'image', type=str)
