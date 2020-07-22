from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_blog import db
from flask_blog.models.entries import User
from flask_blog.views import auth_service
import datetime

view = Blueprint('view', __name__)

auth = Blueprint('auth', __name__)


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = auth_service.login(request.form)
        if not user:
            flash('メールアドレスもしくはパスワードに誤りがあります。')
            return render_template('login.html')
        flash('ログインしました。')
        return redirect(url_for('entry.show_entries'))
  

@view.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        user = auth_service.signup(request.form)
        if user:
            flash('メールアドレスは既に登録されています。')
            return render_template('signup.html')
        flash('新規登録に成功しました。')
        return redirect(url_for('index'))