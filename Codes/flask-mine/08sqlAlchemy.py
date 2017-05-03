# -*- coding:UTF-8 -*-
# 这个文件学学使用Flask-SQLAlchemy来处理数据库
# 1. 指定使用的数据库类型 - 保存在SQLALCHEMY_DATABASE_URI键中
# 2. SQLALCHEMY_COMMIT_ON_TEARDOWN设置为True，每次请求结束都会自动提交数据库中的变动

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 下面的import都是老代码，可以不管
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

# 设置数据库基本参数
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app) # 这个东东就是数据库实例，通过操纵它操纵数据库
# --- 设置结束 ---

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
manager = Manager(app)
bootstrap = Bootstrap(app)


class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        oldName = session.get('name')
        if oldName is not None and oldName != form.name.data:
            flash('change name ummhuuu')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index-flash.html', form = form, name = session.get('name'))

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
