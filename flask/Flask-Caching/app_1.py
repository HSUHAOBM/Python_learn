# 緩存 紀錄值,靜態網頁

from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

@app.route('/')
@cache.cached(timeout=60)
def index():
    return 'This page is cached for 60 seconds.'

@app.route('/get_cached_value')
def get_cached_value():
    cached_value = cache.get('my_cached_value')
    if cached_value is None:
        return 'No cached value found.'
    return f'The cached value is {cached_value}.'

@app.route('/cache_value')
def cache_value():
    cache.set('my_cached_value', 'hello, world!', timeout=60)
    return 'Cached value set.'

@app.route('/index')
@cache.cached(timeout=60)
def index_web():
    return render_template('index.html')

@app.route('/refresh_cache')
def refresh_cache():
    cache.clear()
    return 'Cache cleared'

if __name__ == '__main__':
    app.run(debug=True)