# -*- coding:UTF-8 -*-

from . import db

# 这里引入加密库
from werkzeug.security import generate_password_hash, check_password_hash

# 这里引入了记录用户登录状态的库
from flask_login import UserMixin

# 8.4 描述如何捞到指定用户的回调函数 - login_manager需要实现的方法
from . import login_manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) # 返回用户对象，没有返回None

# 定义两个表 - 通过定义类的方式
class Role(db.Model):
    __tablename__ = 'roles' # 这个变量定义了在数据库中使用的表名
    id = db.Column(db.Integer, primary_key = True) # 参数一： 类型， 参数二： 选项（见P48页）
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role') # 设置一对多， backref参数向user模型中添加了一个属性 - role

    def __repr__(self): # 可选方法，同iOS类的description方法
        return '<Role %r>' % self.name

class User(UserMixin, db.Model): # 8.4注释：传说中的多继承？
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键，关联roles表中的id值
    email = db.Column(db.String(64), unique = True, index = True)

    # 学习用户认证的童鞋看这里
    password_hash = db.Column(db.String(128))
    @property # - 这里学习get、set方法的定义
    def password(self, password):
        raise AttributeError('password is not a readable attribute')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 这里定义一个成员方法
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %>' % self.username
