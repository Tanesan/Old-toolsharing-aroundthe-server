from flask_login import login_user
from sqlalchemy.exc import SQLAlchemyError
from flask_blog import db
from flask_blog.models.entries import User


# 新規登録を行うためのメソッドです。引数にはviewsで取得するformデータが送られてきます。
def signup(data: {}) -> User:
    try:
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        # ユーザーがすでに登録されているかどうかを確認します
        user = User.query.filter_by(email=email).first()
        if user:
            # 同じメールアドレスでユーザーが登録されているのであればユーザーをリターンします
            return user
        # ユーザーがいなければ作成します
        new_user = User.from_args(name, email, password)
        # データベースに追加するところ
        db.session.add(new_user)
        db.session.commit()
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError


def login(data: {}) -> User:
    try:
        email = data.get('email')
        password = data.get('password')
        remember = True if data.get('remember') else False
        user = User.query.filter_by(email=email).first()
        # ユーザーとパスワードの確認
        if not user and not user.check_password(user.password, password):
            raise SQLAlchemyError

        # ログイン。rememberにチェックを入れていればログインが維持される
        login_user(user, remember=remember)
        return user
    except SQLAlchemyError:
        raise SQLAlchemyError