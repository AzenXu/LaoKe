#!/usr/bin/env python
# 上面一行的作用 - 直接使用./manager.py执行脚本，而不需要使用python manager.py - shebang声明

import os
from app import create_app, db # 从app这个文件夹下，找到creat_app和db包含进来
from app.models import User, Role # 从app下的models模块 - 文件， 找到User和Role引进来
from flask_script import Manager, Shell # 引进来命令行管家
from flask_migrate import Migrate, MigrateCommand # 数据库迁移

app = create_app(os.getenv('FLASK_CONFIG') or 'default') # 从环境变量里读取配置名或使用default

# 初始化
manager = Manager(app)
migrate = Migrate(app, db)

# 为Shell配置数据库，和数据库数据库迁移 - 可以直接通过Shell便捷的操纵数据库
def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# 这里的配置是为了单元测试可以跑起来
@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
