# -*- coding: UTF-8 -*-

from flask import render_template, session, redirect, url_for, flash, abort

from . import main
from .forms import NameForm # 从当前目录forms这个文件夹里，引入NameForm这个类
from .. import db # 从上一级目录下引入db这个对象
from ..models import User, Permission  # 从上一级models这个文件夹里，引入User这个类

from flask_login import login_required  # 这里演示8.4保护路由 - 只能登录用户访问

from ..decorators import permission_required, admin_required  # 这里测试权限装饰器

# 演示注册一个受保护的路由
@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed'

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

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

# 下面两个路由测试装饰器
@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return 'For adminstrators!'

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return 'For comment moderators!'

