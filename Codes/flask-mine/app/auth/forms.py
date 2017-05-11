# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, length, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in') # 复选框
    submit = SubmitField('Log In')
