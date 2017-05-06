import unittest
from flask import current_app
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    # 在各个测试前运行
    def setUp(self):
        # 创建测试环境
        # 使用测试配置创建程序
        self.app = create_app('testing')
        # 激活上下文 - 确保能在测试中使用current_app
        self.app_context = self.app.app_context()
        self.app_context.push()
        # 创建一个全新的数据库
        db.create_all()

    # 在各个测试结束后运行
    def tearDown(self):
        # 删除数据库
        db.session.remove()
        db.drop_all()
        # 删除app上下文
        self.app_context.pop()

    # 用例一 - 用例的名字，以test_作为开始
    # 作用 - 确保程序实例存在
    def test_app_exists(self):
        self.assertFalse(current_app is None)

    # 用例二
    # 作用 - 确保程序在测试环境中运行
    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
