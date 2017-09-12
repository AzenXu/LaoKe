# coding=utf8

from flask_wtf import FlaskForm  # 导入Form基类
from wtforms import StringField, SubmitField, TextAreaField, SelectField, BooleanField  # 导入字段
from wtforms.validators import Required, Length, Email, Regexp, ValidationError  # 导入验证方式
from ..models import Role, User
from flask_pagedown.fields import PageDownField


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


class EditProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('where you from', validators=[Length(0, 64)])
    about_me = TextAreaField('blabla')
    submit = SubmitField('done')


class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters, '
                                                                                     'numbers, dots or underscores')])
    confirmed = BooleanField('Confirmed')
    role = SelectField('Role', coerce=int)  # 对应HTML中的<select>表单控件，选项必须是一个元组的列表 - (选项标志符，显示的文本字符串) coerce-> 指定值的类型
    name = StringField('Real name', validators=[Length(0, 64)])
    location = StringField('Location', validators=[Length(0, 64)])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')

    def __init__(self, user, *args, **kwargs):  # 构造方法中传入并保存user，以便做下面的自定义验证
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.order_by(Role.name).all()]  # 为role选项表设置元组选项
        self.user = user

    # 自定义email的检测函数，保证修改之后，email不和其他用户冲突
    def validate_email(self, field):
        if field.data != self.user.email and User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    # 自定义username的检测函数，保证修改之后，email不和其他用户冲突
    def validate_username(self, field):
        if field.data != self.user.username and User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class PostForm(FlaskForm):
    body = PageDownField("What`s on your mind?", validators=[Required()])
    submit = SubmitField('Submit')
