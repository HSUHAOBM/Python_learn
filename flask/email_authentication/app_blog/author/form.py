from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators, SubmitField, PasswordField, EmailField, ValidationError
from app_blog.author.model import UserReister


class FormRegister(FlaskForm):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=25)])

    email = StringField('Email Address', [
        validators.DataRequired(),
        validators.Length(min=6, max=35)])

    password = PasswordField('PassWord', validators=[
        validators.DataRequired(),
        validators.Length(5, 10),
        validators.EqualTo('password2', message='PASSWORD NEED MATCH')
    ])
    password2 = PasswordField('Confirm PassWord', validators=[
        validators.DataRequired()
    ])

    accept_rules = BooleanField('I accept the site rules', [validators.InputRequired()])
    submit = SubmitField('Register New Account')

    # 驗證是否使用過
    def validate_email(self, field):
        if UserReister.query.filter_by(email=field.data).first():
            raise ValidationError('Email already register by somebody')

    def validate_username(self, field):
        if UserReister.query.filter_by(username=field.data).first():
            raise ValidationError('UserName already register by somebody')