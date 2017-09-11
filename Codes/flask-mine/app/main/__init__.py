# -*- coding: UTF-8 -*-

# 模块里的__init__.py文件是让模块可以通过 .main这种形式包含进来的
# main的作用 - 管理View的

from flask import Blueprint

from app.models import Permission

main = Blueprint('main', __name__)  # 创建蓝本 - 蓝本名字， 蓝本所在的包

from . import views, errors


# 导入进来，就意味着这两个文件中的代码会被执行！这和编译型语言非常不同...

#  使用上下文处理器，让模板可能检查权限
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
