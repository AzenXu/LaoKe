# -*- coding: UTF-8 -*-

from flask import render_template, session, redirect, url_for, flash, abort

from . import main
from .forms import NameForm, EditProfileForm, EditProfileAdminForm, PostForm  # 从当前目录forms这个文件夹里，引入NameForm这个类
from .. import db # 从上一级目录下引入db这个对象
from ..models import User, Permission, Role, Post  # 从上一级models这个文件夹里，引入User这个类

from flask_login import login_required, current_user  # 这里演示8.4保护路由 - 只能登录用户访问

from ..decorators import permission_required, admin_required  # 这里测试权限装饰器

# 演示注册一个受保护的路由
@main.route('/secret')
@login_required
def secret():
    return 'Only authenticated users are allowed'

@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARITICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object()) # Post需要的是真正的user对象，current_user是对user的轻度包装，所以需要通过_get_current_object获取真正的对象
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestmp.desc()).all()
    return render_template('index_with_posts.html', form=form, posts=posts)

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('done')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/edit-profile/<int:id>', methods=['GET','POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)

@main.route('/oldhome', methods=['GET', 'POST'])
def indexold():
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

