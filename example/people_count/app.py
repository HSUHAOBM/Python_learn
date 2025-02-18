from flask import Flask, request, jsonify, render_template
from datetime import datetime, date, timedelta
import sqlite3

app = Flask(__name__)
DATABASE = 'visits.db'

def create_table():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute(
            '''
                CREATE TABLE IF NOT EXISTS visits
                (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT UNIQUE,
                    total_count INTEGER,
                    last_visited TEXT
                )
            '''
        )

        cur.execute('CREATE INDEX IF NOT EXISTS ip_index ON visits (ip)')
        cur.execute('CREATE INDEX IF NOT EXISTS date_index ON visits (last_visited)')

def record_visit(ip_address):
    with sqlite3.connect(DATABASE) as con:

        today = date.today().strftime('%Y-%m-%d')
        # test
        # yesterday = (date.today() - timedelta(days=0)).strftime('%Y-%m-%d')
        # today = (date.today() + timedelta(days=-1)).strftime('%Y-%m-%d')

        cur = con.cursor()
        # 新增 IP, 並計算 total_count(當日重複不算), 紀錄最後登入日期
        cur.execute(
            """INSERT OR REPLACE INTO visits
            (ip, total_count, last_visited)
            VALUES (?,
                COALESCE((
                        SELECT total_count + 1 FROM visits
                        WHERE ip = ? AND last_visited != ?), 1), ?)""",
            (ip_address, ip_address, today, today)
        )
def get_visit_count():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        cur.execute('SELECT SUM(total_count) FROM visits')
        count = cur.fetchone()[0]
        return count

def get_daily_visit_count():
    with sqlite3.connect(DATABASE) as con:
        cur = con.cursor()
        date_str = date.today().strftime('%Y-%m-%d')
        cur.execute('SELECT COUNT(DISTINCT ip) FROM visits WHERE last_visited = ?', (date_str,))
        count = cur.fetchone()[0]
        return count

@app.route('/')
def index():
    # test
    # ip_address = '127.0.0.2'

    ip_address = request.remote_addr
    record_visit(ip_address)
    count = get_visit_count()
    daily_count = get_daily_visit_count()
    return f'Total visits: {count}, Daily visits: {daily_count}'

@app.route('/visits')
def visits():
    ip_address = request.remote_addr
    record_visit(ip_address)
    count = get_visit_count()
    daily_count = get_daily_visit_count()
    return jsonify({'total_visits': count, 'daily_visits': daily_count})

    # return render_template('upload.html')

@app.route('/people')
def people_counts():
    return render_template('index.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)