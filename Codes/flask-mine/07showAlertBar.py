# -*- coding:UTF-8 -*-
# 这个文件用来演示设置一个alertBar - flash()函数
# 同时需要配合模板设置flash的渲染效果 - 通过get_flashed_messages()函数获取flash出来的内容

from flask import Flask
from flask import flash

# 下面的import都是老代码，可以不管
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
        oldName = session.get('name')
        if oldName is not None and oldName != form.name.data:
            flash('change name ummhuuu') # 看样子这个flash也会把内容存起来，下次渲染的时候在模板中取出来...
            # 并不是实时刷新view的样子呢
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
