# coding=utf8
from functools import wraps
from flask import abort
from flask_login import current_user

from app.models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_funciton(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)  # 用法来自functools这个包
            return f(*args, **kwargs)
        return decorated_funciton
    return decorator

def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)