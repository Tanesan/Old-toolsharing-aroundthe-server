from flask_login import login_user
from sqlalchemy.exc import SQLAlchemyError
from flask_blog import db
from flask_blog.models.entries import User
#login_user(user, remember=remember)
def login(data: {}) -> User:
    email = data.get('email')
    password = data.get('password')
    remember = True if data.get('remember') else False
    user = User.query.filter_by(email=email).first()
    return user


def signup(data: {}) -> User:
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    user = User.query.filter_by(email = email).first()
    if user:
        return user
    new_user = User.from_args(name, email, password)
    db.session.add(new_user)
    db.session.commit()
    return user