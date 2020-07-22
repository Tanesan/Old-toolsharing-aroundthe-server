from flask import Flask
#from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
#CORS(app)
#app.config.from_object('flask_blog.config')

app.secret_key = "super secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///qa-site.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

from flask_blog.views.views import view
app.register_blueprint(view)

from flask_blog.views.entries import entry
app.register_blueprint(entry, url_prefix='/users')

from flask_blog.models.entries import User

login_manager = LoginManager()
login_manager.login_view = 'views.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# authに関するルーティングを追加
from flask_blog.views.views import view
 
# authに関するルートをflaskアプリであるappに追加
app.register_blueprint(view)