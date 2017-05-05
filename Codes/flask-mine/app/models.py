from . import db

# 定义两个表 - 通过定义类的方式
class Role(db.Model):
    __tablename__ = 'roles' # 这个变量定义了在数据库中使用的表名
    id = db.Column(db.Integer, primary_key = True) # 参数一： 类型， 参数二： 选项（见P48页）
    name = db.Column(db.String(64), unique = True)
    users = db.relationship('User', backref='role') # 设置一对多， backref参数向user模型中添加了一个属性 - role

    def __repr__(self): # 可选方法，同iOS类的description方法
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True, index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 设置外键，关联roles表中的id值

    def __repr__(self):
        return '<User %>' % self.username
