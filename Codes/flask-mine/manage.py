#!/usr/bin/env python
# -*- coding:UTF-8 -*-

# 上面一行的作用 - 直接使用./manager.py执行脚本，而不需要使用python manager.py - shebang声明
# 注意：在跑程序之前，一定要保证数据库已经创建好了...
# 创建数据库的命令：python manage.py db upgrade

import os
from app import create_app, db  # 从app这个文件夹下，找到creat_app和db包含进来
from app.models import User, Role, Post  # 从app下的models模块 - 文件， 找到User和Role引进来
from flask_script import Manager, Shell  # 引进来命令行管家
from flask_migrate import Migrate, MigrateCommand  # 数据库迁移

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # 从环境变量里读取配置名或使用default

# 初始化
# Flask-script初始化 - 作用是方便通过命令行给flask配置启动参数，不用写死在代码里
manager = Manager(app)
# 说明：migrate这个库的作用是用来更新表结构 - 数据库迁移框架
# 老方法：删除旧表，创建新表 - 问题：数据丢失了
# migrate的原理：类似源码版本管理工具，跟踪数据库表的变化，然后增量式的把变化应用到新表中
# 迁移框架：Alembic，Migrate是对这个框架的轻量级包装，并把包装集成到flask-script中，所有操作可以通过flask-script完成
migrate = Migrate(app, db)

# 为Shell配置数据库，和数据库数据库迁移 - 可以直接通过Shell便捷的操纵数据库
# 类似于一个协议函数，作用是通过命令行启动程序的时候，自动导入指定的表
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post)
manager.add_command("shell", Shell(make_context=make_shell_context))  # 可以直接通过python manage.py shell启动shell模式，同时自动导入数据库
manager.add_command('db', MigrateCommand)  # 第6行的命令可以实现，就是在这里配置的 - 猜测遇到db指令就会调用MigrateCommand，做数据库迁移相关

# 这里的配置是为了单元测试可以跑起来
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
