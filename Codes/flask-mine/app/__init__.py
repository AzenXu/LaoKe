# 这是一个构造函数，app对象从这里生成，以方便进行配置
# 在这里导入需要用到的库，但是不初始化（仅实例化），因为app还没生成

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config # 导入自定义的config字典

from flask import Blueprint # 需要引入蓝本，以遍在工厂方法中定义路由和错误页

main = Blueprint('main', __name__) # 参数一：蓝本的名字； 参数二：蓝本所在的包或模块

from . import views, errors # views.py中保存程序的路由，errors.py中保存错误处理


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

# 实现工厂函数，创建app实例
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)

    # 之后需要定义路由和错误页了...但是有问题！
    # 需要使用蓝本定义路由
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
