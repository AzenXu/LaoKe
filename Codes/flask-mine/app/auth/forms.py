# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, length, Email, regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), length(1, 64), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in') # 复选框
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), length(1, 64), regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'Usernames must have only letters,numbers,dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    # 如果定义了以validate_开头且后面跟着「字段名」的方法，这个方法就和验证函数一起调用
    # 定义了email的验证函数
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            # 通过抛ValidationError的方式来验证失败
            raise ValidationError('Email alread registered.')
    # 定义了username的验证函数
    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use.')
