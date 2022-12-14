from itsdangerous import TimedJSONWebSignatureSerializer
from itsdangerous import SignatureExpired, BadSignature
from flask import current_app
from app_blog import db, bcrypt

class UserReister(db.Model):
    __tablename__ = 'UserRgeisters'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(50), nullable=False)
    confirm = db.Column(db.Boolean, default=False)

    # property 只能讀取的屬性特性 // 配合 setter、getter、deleter
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf8')

    # 密碼驗證 return: True/False
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'username:%s, email:%s' % (self.username, self.email)

    # 建立認證 itsdangerous
    def create_confirm_token(self, expires_in=3600):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'user_id': self.id})

    # 驗證 token
    def validate_confirm_token(self, token):
        s = TimedJSONWebSignatureSerializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            #  時間超過
            return False
        except BadSignature:
            #  驗證錯誤
            return False
        # {'user_id': self.id}
        return data