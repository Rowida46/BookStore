from flask_restful import fields
AuthSerilizer = {
    'id': fields.Integer,
    'title': fields.String,
}

bookSerilizer = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'image': fields.String,
}
