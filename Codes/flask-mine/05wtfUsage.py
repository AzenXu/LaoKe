# -*- coding:UTF-8 -*-
# 这个文件用来演示使用wtf表单
# 1. 配置密钥保证表单数据安全
# 原理 - 设置一个密钥，用这个密钥生成加密令牌，用令牌验证请求数据的真伪
# 2. 使用Form子类来实现Web表单
# 配合template/index食用更加

from flask import Flask

from flask_wtf import Form #导入Form基类
from wtforms import StringField, SubmitField #导入字段
from wtforms.validators import Required #导入验证方式


# 下面的import都是老代码，可以不管
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
from flask import render_template
from flask_bootstrap import Bootstrap
#-------

# 定义一个TextField
# 有一个name的文本字段和一个submit的提交按钮
# StringField -> 属性为type = 'text'的<input> validators -> 一个由验证函数组成的列表
# SubmitField -> 属性为type = 'submit'的<input>
# 所以这个类其实是一个UI组件对象？ - 不，这个类更像一个ViewModel，只是绑定已经默认做好了
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'security key' #用这个字典存key - SECRET_KEY配置通用密钥
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/', methods = ['GET', 'POST'])
def index():
    # 实例化一个Form，传给模板，让它渲染 {{ wtf.quick_form(form) }}
    # 这个思路蛮不错的...和iOS思路有区别. iOS的UI控件怎么展示，是控件自己决定的，这里
    # 展示的样式是由渲染引擎决定的...所以NameForm其实是一个ViewModel
    # 输入框里的内容改变后，会改变VM的属性值，所以通过属性值可以拿到输入的name
    form = NameForm() # 如果是POST请求，这里会被自动赋值的吧...
    name = None
    # 提交表单后，如果数据通过验证，则函数返回True
    # 会调用name字段上附属的Required()验证函数
    if form.validate_on_submit():
        name = form.name.data
        # 清空表单 - 这也是VM的特点，值变了view的值自动变
        form.name.data = ''
    return render_template('index.html', form = form, name = name)

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
