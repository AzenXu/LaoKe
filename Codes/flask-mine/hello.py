# -*- coding:UTF-8 -*-
# 这个文件学学使用Flask-Mail提供电子邮件支持 - 特定事件发生的时候，给用户发邮件提醒用户
# 库 - Python标准库中的smtplib包 - Flask-Mail包装了这个包
# Flask-Mail连接到SMTP服务器，把邮件交给这个服务器发送
# 不配置，会连接localhost上的port25，无需验证即可发邮件

from flask import Flask
from flask_mail import Mail
from flask_mail import Message

# 下面的import都是老代码，可以不管
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_sqlalchemy import SQLAlchemy
import os
from flask_script import Shell # 不用每次执行Python shell都import db
from flask import flash
from flask import session
from flask import redirect
from flask import url_for
from flask_wtf import Form #导入Form基类
from wtforms import StringField, SubmitField #导入字段
from wtforms.validators import Required #导入验证方式
from flask import request
from flask import make_response
from flask import abort
from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
#-------

app = Flask(__name__)

# 配置电子邮件信息

app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASKY_MAIL_SENDER'] = 'Azen Admin <azen_me@163.com>'

app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('FLASK_MAIL_NAME')
app.config['MAIL_PASSWORD'] = os.environ.get('FLASK_MAIL_PASSWORD')

# --- 邮件配置完毕 ---

mail = Mail(app) # 可以使用Python Shell发送邮件了，还可以写到程序里，这里木有做。

# 设置数据库基本参数
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True # 修改数据自动commit
db = SQLAlchemy(app) # 这个东东就是数据库实例，通过操纵它操纵数据库
# --- 设置结束 ---

manager = Manager(app) # Flask-Script的manager
bootstrap = Bootstrap(app)

# 设置migrate数据库迁移
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
# ---


# 定义两个表 - 通过定义类的方式
class Role(db.Model):
    __tablename__ = 'roles' # 这个变量定义了在数据库中使用的表名
    id = db.Column(db.Integer, primary_key = True) # 参数一： 类型， 参数二： 选项（见P48页）
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role') # 设置一对多， backref参数向user模型中添加了一个属性 - role

    def __repr__(self): # 可选方法，同iOS类的description方法
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键，关联roles表中的id值

    def __repr__(self):
        return '<User %>' % self.username

app.config['SECRET_KEY'] = 'security key'

# 设置Python Shell的便捷用法 - 执行python shell的时候不用每次都import db
def make_shell_context():
    return dict(app = app, db = db, User = User, Role = Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
# 想尝试Python Shell的写法，参考P50，sqlOperactionExe.py文件
# --- 设置结束 ---


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first() # 捞

        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            # db.session.commit() - 前面配置了app.config所以这里会自动commit
            session['known'] = False
            flash('first time here? welcome~~') # 捞不到创建
        else:
            session['known'] = True

        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index-sqltest.html',
                           form = form, name = session.get('name'),
                           known = session.get('known', False))

# ------------下面都是老代码，可以不看-----------

@app.route('/user/<name>')
def user(name):
    #第一个参数是文件名，后面的参数都是键值对，表明模板中的参数名对应的真实值
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/request')    #把response拼成一个对象返回。注意需要导入make_response
def errorShowRequest():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/error')
def errorShow():
    return '<h1>error!!!<h1>', 400

@app.route('/abort')
def abortTest():
    if True:
        abort(404)  # 注意import abort, 这里直接抛异常
    return '<h1>这句不可能执行到</h1>'

@app.route('/redirect') #返回一个302重定向指令，需要import redirect
def redirectShow():
    return redirect('http://azen.me')



if __name__ == '__main__':
    manager.run()
