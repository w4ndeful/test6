from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

CATEGORIES = [('tech', 'Tech'), ('science', 'Science'), ('lifestyle', 'Lifestyle')]

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices=CATEGORIES, validators=[DataRequired()])
    is_active = BooleanField('Active')
    submit = SubmitField('Add Post')
