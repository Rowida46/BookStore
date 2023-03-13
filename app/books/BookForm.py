from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileRequired, FileAllowed

# from app.authers.models import Author

# auths = Author.query.all()


class BookForm(FlaskForm):
    title = StringField("book title", validators=[DataRequired()])
    description = StringField("Book Description", validators=[DataRequired()])
    rate = IntegerField("Rate")
    image = FileField("Book image", validators=[DataRequired()])
    auth = SelectField('Auth', coerce=int, choices=[])
