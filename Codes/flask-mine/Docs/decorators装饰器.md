从下面的代码中分析下所谓的装饰器：

```python
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_funciton(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_funciton
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)
```

装饰器这个东东可以理解为闭包。

上面一段实现的功能是：有xxx权限才能执行函数里的操作。

从```return permission_required(Permission.ADMINISTER)(f)```这里可以看出，通用方法的调用方式类似：


```
permission_required(Permission.ADMINISTER)(
    print xxx...
)
```

是不是和OC的block很像：定义了一个block{print xxx...}，这个block的参数是Permission.ADMINISTER

上面的理解都很片面，看了下面的用法就更好理解了：

```python
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
```

现在访问http://localhost:5000/admin试试~
