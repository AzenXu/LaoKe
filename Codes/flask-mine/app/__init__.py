# -*- coding:UTF-8 -*-

# 这是一个构造函数，app对象从这里生成，以方便进行配置
# 在这里导入需要用到的库，但是不初始化（仅实例化），因为app还没生成

# 这里引入记录登录状态的库 - 书8.4节
from flask_login import LoginManager

# --- 下面是旧的 ---
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config # 导入自定义的config字典

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

#登录状态记录
login_manager = LoginManager()
# 设为strong会记录客户端IP和浏览器的用户代理信息，发现异常就登出
login_manager.session_protection = 'strong'
# 设置登录页面的端点 - auth.这个是定义了路由的蓝本的名字
login_manager.login_view = 'auth.login'

# 实现工厂函数，创建app实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    login_manager.init_app(app)

    # 使用蓝本定义路由 - 蓝本描述了路由和错误处理
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 注册用户蓝本
    from .auth import auth as auth_blueprint
    # url_prefix参数 - 以后在蓝本中定义的所有路由，都会加上指定的前缀
    # 如: /login路由会注册成/auth/login
    # 对应的url: http://localhost:5000/auth/login
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
