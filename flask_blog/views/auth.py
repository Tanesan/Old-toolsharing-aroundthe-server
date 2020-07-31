from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_blog.services import auth_service
import time
from flask import jsonify
from flask import json
from flask_blog import app

auth = Blueprint('auth', __name__)
res = {}
@auth.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Content-Type', 'application/json')
  return response

@auth.route('/auth/api', methods=['GET', 'POST'])
def login():
    user = auth_service.login(request.json)
    print(user)
    if not user or user == False:
      res['auth'] = False;
      return jsonify(res)
    res['auth'] = True;
    return jsonify(res)

 #   return request.get_data()
#  if request.method == 'GET':
    #  return redirect('http://localhost:3000/')
 # else:
   # text = request.get_data




@auth.route('/auth/api/signup', methods=['GET', 'POST'])
def signup():
        user = auth_service.signup(request.json)
        if user:
            res['auth'] = False;
            return jsonify(res)
        res['auth'] = True;
        return jsonify(res)