from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class Character_Form(FlaskForm):
    name = StringField("Name", validators=[DataRequired()]) 
    submit = SubmitField('Submit')
