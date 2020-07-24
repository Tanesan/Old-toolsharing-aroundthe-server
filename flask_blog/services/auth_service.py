from flask_login import login_user
from sqlalchemy.exc import SQLAlchemyError
from flask_blog import db
from flask_blog.models.user import User

"""
servicesのファイルは全てデータベースにデータを送るための準備をしたり、
データに何かしらの処理を与えるコードを記述する場所です。
"""


# 新規登録を行うためのメソッドです。引数にはviewsで取得するformデータが送られてきます。
def signup(data) -> User: 
    try:
        name = data['name']
        email = data['email']
        password = data['password']
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        new_user = User.from_args(name, email, password)
        db.session.add(new_user)
        db.session.commit()
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError


def login(data) -> User:
    try:
        email = data['email']
        password = data['password']
        remember = True if data['remenber']=="remenber" else False
        user = User.query.filter_by(email=email).first()
        # ユーザーとパスワードの確認
        if not user and not user.check_password(user.password, password):
            raise SQLAlchemyError

        # ログイン。rememberにチェックを入れていればログインが維持される
        login_user(user, remember=remember)
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError