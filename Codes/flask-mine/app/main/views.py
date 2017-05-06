# -*- coding: UTF-8 -*-

from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm # 从当前目录forms这个文件夹里，引入NameForm这个类
from .. import db # 从上一级目录下引入db这个对象
from ..models import User # 从上一级models这个文件夹里，引入User这个类

@main.route('/', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index')) # 蓝本里使用url_for函数，要通过蓝本名.index()视图函数的URL使用url函数
        # .index是main.index的简写形式 -> 省略蓝本名
    return render_template('index-sqltest.html',
                           form = form, name = session.get('name'),
                           known = session.get('known', False))