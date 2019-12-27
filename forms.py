from flask_wtf import FlaskForm
from myproject.model import User
from wtforms import SubmitField,PasswordField,StringField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError



class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = StringField('Password')
    submit = SubmitField("submit")





class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired(),EqualTo('pass_confirm',message = "password must match")])
    pass_confirm = PasswordField('confirm password',validators=[DataRequired()])
    submit = SubmitField('submit')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def check_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('username is taken')

