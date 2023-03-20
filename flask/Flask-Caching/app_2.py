# 緩存 紀錄登入狀態

from flask import Flask, session
from flask_caching import Cache

app = Flask(__name__)
app.secret_key = 'secret_key'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
def index():
    return 'Home Page'

@app.route('/login')
def login():
    session['user_id'] = 1
    cache.set(f'user:{1}:status', 'logged_in', timeout=3600)
    return 'Login Success'

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    cache.delete(f'user:{1}:status')
    return 'Logout Success'

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if user_id is None:
        return 'Login Required'
    status = cache.get(f'user:{user_id}:status')
    if status != 'logged_in':
        return 'Login Required'
    return 'Dashboard'

if __name__ == '__main__':
    app.run(debug=True)