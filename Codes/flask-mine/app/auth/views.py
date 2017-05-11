# -*- coding: UTF-8 -*-

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from flask_login import logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # 根据email捞用户
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            # 记住我 - 如果为True，会在浏览器里写入一个长期有效的cookie
            # 这个Cookie可以复现用户会话
            login_user(user, form.remember_me.data)
            # 这里注意：当用户没登录且访问一个需要登录的界面时，会把原地址存在request.args的next里
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))
