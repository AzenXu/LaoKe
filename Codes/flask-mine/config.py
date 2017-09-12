# -*- coding:UTF-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Config基类 - 包含通用配置
# 子类分别定义专用的配置
# 从环境变量中导入的好处：安全、灵活
# init_app()类方法，参数是程序实例，这个方法中执行对当前环境的配置初始化

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'security key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束后都会自动提交数据库中的变动
    #  邮件相关
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Azen Admin <azen_me@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #  文章分页相关
    FLASKY_POSTS_PER_PAGE = 10

    @staticmethod  # 常量方法，不同实例化这个类就能调用的方法
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('FLASK_MAIL_NAME')
    MAIL_PASSWORD = os.environ.get('FLASK_MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = 'azen_me@163.com'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
