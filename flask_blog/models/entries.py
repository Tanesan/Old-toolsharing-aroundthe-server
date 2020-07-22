from flask_blog import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text) 
 
# モデルに関する設定
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(1000))
    password = db.Column(db.String(100))
 
    # モデルからインスタンスを生成するときに使います。(利便性を高めるため)
    # passwordの暗号化も自動で行うことができるので、安全性も高めることができます。
    @classmethod
    def from_args(cls, name: str, email: str, password: str):
        instance = cls()
        instance.name = name
        instance.email = email
        if password is not None:
            # passwordがあれば暗号化します。
            instance.hash_password(password)
        return instance
 
    # 暗号化するためのメソッド。
    def hash_password(self, clean_password):
        self.password = generate_password_hash(str(clean_password), method='sha256')
 
    # 登録したpasswordとユーザーがログインフォームで入力したパスワードが正しいかどうかのチェックを行うメソッド
    def check_password(self, clean_password):
        return check_password_hash(self.password, clean_password)
