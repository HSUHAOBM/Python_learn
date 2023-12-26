from flask import Flask, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

# 定義用戶類別
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return f"User(id='{self.id}', username='{self.username}')"

# 假設以下是應用程式中的用戶
users = [
    User(1, 'user1', 'password1'),
    User(2, 'user2', 'password2')
]
username_table = {u.username: u for u in users}

# 身份驗證函數，通過驗證返回用戶對象，否則返回 None
def authenticate(username, password):
    for user in users:
        if user.username == username and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
            return user

# 根據用戶對象生成 JWT token
def identity(payload):
    user_id = payload['identity']
    for user in users:
        if user.id == user_id:
            return user

# 創建 Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['JWT_AUTH_HEADER_PREFIX'] = 'Bearer'  # 設置 JWT 標頭前綴
jwt = JWT(app, authenticate, identity)

# 路由，需要 JWT token 才能訪問
@app.route('/protected')
@jwt_required()
def protected():
    return jsonify({'user': str(current_identity)}), 200

# 路由，需要用戶名和密碼登錄以獲取 JWT token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    user = authenticate(username, password)
    if not user:
        return jsonify({'message': 'Invalid credentials', 'authenticated': False}), 401

    # 用戶驗證成功，返回 JWT token
    token = jwt.jwt_encode_callback({'identity': user.id})
    return jsonify({'token': token.decode('utf-8')})

if __name__ == '__main__':
    app.run(debug=True)