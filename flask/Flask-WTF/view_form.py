
from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField, PasswordField, EmailField, ValidationError


#  從繼承FlaskForm開始
class UserForm(FlaskForm):
  username = StringField('UserName', validators=[validators.DataRequired(message='Not Null')])
  email = EmailField('Email', validators=[validators.DataRequired(message='Not Null')])
  submit = SubmitField('Submit')

  # 驗證
  def validate_username(self, field):
    if 'H' not in field.data:
      raise ValidationError(" name have 'H' ")
