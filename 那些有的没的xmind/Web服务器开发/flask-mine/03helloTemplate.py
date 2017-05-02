# -*- coding:UTF-8 -*-
# 这个文件用来演示模板文件的使用 - 联合templates文件夹一起食用风味更佳

from flask import Flask
from flask import render_template   # 引入模板渲染引擎

# 下面的import都是老代码，可以不管
from flask import request
from flask import make_response
from flask import redirect
from flask import abort
from flask_script import Manager
#-------

app = Flask(__name__)

# 初始化flask-script的manager实例，将app传进来
manager = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    #第一个参数是文件名，后面的参数都是键值对，表明模板中的参数名对应的真实值
    return render_template('user.html', name=name)

# ------------下面都是老代码，可以不看-----------

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
