# -*- coding:UTF-8 -*-

import os
from datetime import datetime

from . import db

# 这里引入加密库
from werkzeug.security import generate_password_hash, check_password_hash

# 这里引入了记录用户登录状态的库
from flask_login import UserMixin, AnonymousUserMixin

# 8.4 描述如何捞到指定用户的回调函数 - login_manager需要实现的方法
from . import login_manager

# 8.6 确认用户账户
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


# 9.1 用户权限
class Permission:
    def __init__(self):
        pass

    FOLLOW = 1 << 0
    COMMENT = 1 << 1
    WRITE_ARITICLES = 1 << 2
    MODERATE_COMMENTS = 1 << 3
    ADMINISTER = 1 << 7


@login_manager.user_loader  # Flask-Login 要求程序实现一个回调函数，使用指定的标识符加载用户
def load_user(user_id):
    return User.query.get(int(user_id))  # 返回用户对象，没有返回None


# 定义两个表 - 通过定义类的方式
class Role(db.Model):
    __tablename__ = 'roles'  # 这个变量定义了在数据库中使用的表名
    id = db.Column(db.Integer, primary_key=True)  # 参数一： 类型， 参数二： 选项（见P48页）
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')  # 设置一对多， backref参数向user模型中添加了一个属性 - role
    permissions = db.Column(db.Integer)  # 权限列表 - 位运算
    default = db.Column(db.Boolean, default=False, index=True)

    @staticmethod  # 使用一个静态方法生成所有角色信息 - 用法：Shell启动，Role.insert_roles() - 如果不行，尝试干掉数据库文件然后重新生成 - 应该是数据库迁移工具的问题
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARITICLES, True),
            'Moderator': (
            Permission.FOLLOW | Permission.COMMENT | Permission.WRITE_ARITICLES | Permission.MODERATE_COMMENTS, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):  # 可选方法，同iOS类的description方法
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):  # 8.4注释：传说中的多继承？
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 设置外键，关联roles表中的id值
    email = db.Column(db.String(64), unique=True, index=True)

    # 学习用户认证的童鞋看这里
    password_hash = db.Column(db.String(128))

    # 第10章 - 用户资料页
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())  # A variably sized string type. 可变长度字符串
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)  # 默认值为当前时间 - default接收的参数为一个函数 - 这个字段只需要默认值...
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)  # 这个字段每次登录之后都需要更新

    def ping(self):  # 更新last_seen，每次收到用户请求的时候都需要调用ping方法，通过钩子实现这个需求 - before_app_request
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    @property  # - 这里学习get、set方法的定义
    def password(self, password):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 这里定义一个成员方法
    def verify_password(self, password):
        print('---', self.password_hash, '----', generate_password_hash(password), '----')
        return check_password_hash(self.password_hash, password)

    # 学习确认用户账户的同学请看这里
    confirmed = db.Column(db.Boolean, default=False)  # 定义了一个状态 - 是否确认

    # 定义方法 - 生成确认令牌，有效期一小时
    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    # 验证令牌 - 验证通过把新添加的confirm属性设为true
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:  # 当前登录的用户不是待验证的用户
            return False
        self.confirmed = True
        db.session.add(self)
        return True

    def can(self, permissions):
        return self.role is not None and (self.role.permissions & permissions) == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        # 给用户赋值
        if self.role is None:
            if len(Role.query.all()) is 0:
                Role.insert_roles()  # 用户角色表初始化...
            print('---xxx---', os.getenv('FLASK_CONFIG'), '---xxx---')  # 这里取不到东西...为啥？明明配了啊
            admin_mail = 'admin@admin.com'  # 临时写在这里
            if self.email == admin_mail:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    def __repr__(self):
        return '<User %>' % self.username


#  这个类的设计目的是为了不管用户是否登录，都能调用current_user.can方法和is_administrator方法 - 通用性设计
class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

#  配置默认用户所属的类
login_manager.anonymous_user = AnonymousUser
