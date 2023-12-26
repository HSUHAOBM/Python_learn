from flask import Flask, render_template
from flask_moment import Moment
from datetime import datetime, date

app = Flask(__name__)
moment = Moment(app)

@app.route('/')
def index():
    now = datetime.utcnow()
    past_time = date(2018, 1, 1)
    return render_template('index.html', now=now, past_time=past_time)

if __name__ == '__main__':
    app.debug = True
    app.run()