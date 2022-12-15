from flask import Flask
from flask_script import Manager

app = Flask(__name__)

DBScritp = Manager(app)

@DBScritp.command
def init_db():
    print('init database success')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    DBScritp.run()