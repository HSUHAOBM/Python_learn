
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField, PasswordField, EmailField, ValidationError


#  從繼承FlaskForm開始
class UserForm(FlaskForm):
  username = StringField('UserName', validators=[validators.DataRequired(message='Not Null')])
  email = EmailField('Email', validators=[validators.DataRequired(message='Not Null')])
  submit = SubmitField('Submit')