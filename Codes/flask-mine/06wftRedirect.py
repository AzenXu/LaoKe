# -*- coding:UTF-8 -*-
# 这个文件用来演示设置重定向
# 作用：防止提交表单后，点击刷新按钮，表单又提交一次
# 方法：使用重定向作为POST请求的响应，一旦收到个POST请求，就返回一个重定向
# 问题：重定向后，POST发过来的数据不就丢失了？
# 解决：写到session里 - session类似于cookie

from flask import Flask
from flask import session
from flask import redirect
from flask import url_for

# 下面的import都是老代码，可以不管
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

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'security key'
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        # 用session存post过来的信息
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    # 如果session.get取不到值，返回NULL
    return render_template('index.html', form = form, name = session.get('name'))

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
