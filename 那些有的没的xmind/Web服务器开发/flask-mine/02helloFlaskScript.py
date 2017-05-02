# -*- coding:UTF-8 -*-
# 这个文件用来演示Flask-script插件的使用

from flask import Flask
from flask import request # 引入线程级别全局变量 - request以拿到相关参数
from flask import make_response
from flask import redirect # 重定向
from flask import abort # 中断处理 - 返回404用的

from flask_script import Manager #Flask插件都放在flask.ext命名空间下...过期了，现在从flask_script里面引

app = Flask(__name__)

# 初始化flask-script的manager实例，将app传进来
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello, Little black Yo~~ Good Night~~</h1><p>Your Browser if %s</p>' % user_agent

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

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
