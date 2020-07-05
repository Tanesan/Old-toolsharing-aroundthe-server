from flask import Flask
#from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="/templates/toolshare")
#CORS(app)
app.config.from_object('flask_blog.config')

db = SQLAlchemy(app)

from flask_blog.views.views import view
app.register_blueprint(view)

from flask_blog.views.entries import entry
app.register_blueprint(entry, url_prefix='/users')