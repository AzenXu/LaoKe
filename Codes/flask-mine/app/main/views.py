# -*- coding: UTF-8 -*-

from flask import render_template, session, redirect, url_for, flash, abort, request, current_app

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
    # 发布文章按钮点击之后
    if current_user.can(Permission.WRITE_ARITICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object()) # Post需要的是真正的user对象，current_user是对user的轻度包装，所以需要通过_get_current_object获取真正的对象
        db.session.add(post)
        return redirect(url_for('.index'))

    # 判断展示哪些文章 from 12.4
    show_followed = False
    if current_user.is_authenticated:
        # 从cookie里取show_followed字段。request.cookies这是一个字典
        show_followed = bool(request.cookies.get('show_followed',''))
        print('show_followed result = ' + 'show followed' if show_followed else 'show all' + 'request = ' + str(request))
    if show_followed:
        query = current_user.followed_posts
    else:
        query = Post.query

    # posts = Post.query.order_by(Post.timestmp.desc()).all()
    page = request.args.get('page',1,type=int)  #  从请求的查询字符串中获取渲染的页数，没有指定则显示第1页，type=int保证参数无法转换成整数时，返回默认值
    #  paginate: SQLAlchemy的分页控件,返回值是一个Pagination类对象，用于在模板中生成分页链接
    #  进一步理解下分页，其实它类似于一个SQLAlchemy的过滤器...
    pagination = query.order_by(Post.timestmp.desc()).paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    posts = pagination.items
    return render_template('index_with_posts.html', form=form, posts=posts, pagination=pagination)

# 显示所有文章 - from 12.4
@main.route('/all')
@login_required
def show_all():
    from flask import make_response
    resp = make_response(redirect(url_for('.index')))  # 因为要操纵cookie，所以需要手动创建response
    resp.set_cookie('show_followed','',max_age=30*24*60*60)  # 第二个参数为''的时候才为False，0也是True... max_age是一个可选参数，设定cookie的过期时间
    return resp

# 只显示被关注者的文章
@main.route('/followed')
@login_required
def show_followed():
    from flask import make_response
    # 只有通过make_response创建的响应对象，才能
    resp = make_response(redirect(url_for('.index')))
    resp.set_cookie('show_followed','1',max_age=30*24*60*60)

    # 这里不应该用这个redirect - 这样的写法系统自动封装好了response，此处返回自定义的response就好了
    # return redirect(request.args.get('next') or url_for('main.index'))
    return resp

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    posts = user.posts.order_by(Post.timestmp.desc()).all()
    return render_template('user.html', user=user, posts=posts)

@main.route('/post/<int:id>')
def post(id):
    post = Post.query.get_or_404(id)
    return render_template('post.html', posts=[post])

@main.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and not current_user.can(Permission.ADMINISTER):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.body = form.body.data
        db.session.add(post)
        flash('The post has been updated.')
        return redirect(url_for('.post', id=post.id))
    form.body.data = post.body
    return render_template('edit_post.html', form=form)

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

# 关注和取消关注这两个方法，最能体现什么叫「前后端分离」...逻辑要在后端实现 - controller层，展示在前端 - view层
# - view层到controller层的消息传递，这里是用路由的形式实现的
# 关注某人
@main.route('/follow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user.')
        return redirect(url_for('.index'))
    if current_user.is_following(user):
        flash('You are already following this user.')
        return redirect(url_for('.user', username=username))
    current_user.follow(user)
    flash('You are now following' + username)
    return redirect(url_for('.user', username=username))

# 取消关注某人
@main.route('/unfollow/<username>')
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('Invalid user')
        return redirect(url_for('.index'))
    if not current_user.is_following(user):
        flash('You are not his fans')
        return redirect(url_for('.user', username=username))
    current_user.unfollow(user)
    flash('Done! Say goodbye to him')
    return redirect(url_for('.user', username=username))



# 下面两个路由测试自定义装饰器
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

