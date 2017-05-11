from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')
#
# @auth.route('/logout')
# def logout():
#     return render_template('')
