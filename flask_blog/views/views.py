from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_blog import db
import time
from flask_blog.models.entries import User
from flask_blog.views import auth_service
import datetime
from flask import jsonify
from flask import json

view = Blueprint('view', __name__)
res = {}
@app.route('/time')
def get_current_time():
    return {'time': time.time()}

def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('view.login'))
        return view(*args, **kwargs)
    return inner

@app.route('/auth/api', methods=['POST'])
def login():
    # if request.method == 'POST':
     #  return redirect('http://localhost:3000/')
   #  else:
   # text = request.get_data
    
    user = auth_service.login(request.json)
    if not user:
        flash('メールアドレスもしくはパスワードに誤りがあります。')
        res['auth'] = False;
        return jsonify(res)
    res['auth'] = True;
    return jsonify(res)


@view.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('ログアウトしました')
    return redirect(url_for('entry.show_entries'))

@view.app_errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('view.login'))



@view.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        user = auth_service.signup(request.form)
        if user:
            flash('メールアドレスは既に登録されています。')
            return render_template('signup.html')
        flash('新規登録に成功しました。')
        return render_template('login.html')