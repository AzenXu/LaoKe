# -*- coding: UTF-8 -*-

from flask_wtf import FlaskForm #导入Form基类
from wtforms import StringField, SubmitField #导入字段
from wtforms.validators import Required #导入验证方式

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
