from flask import Flask
from flask_script import Manager
# 載入Command
from flask_script import Command
app = Flask(__name__)

DBScritp = Manager(app)

class MyCommand(Command):
    print('MyCommand Class, use flask_script')
    def run(self):
        print('MyCommand Method')
# 註冊自定義的類別
DBScritp.add_command('mycommand', MyCommand())
# python test-script2.py mycommand
# MyCommand Class
# MyCommand Method

# -----------------------------------------------------

# 參數
@DBScritp.option('-n', '--para', help='input parameter')
def param(para):
    print("It's Your parameter %s" % para)
# python test-script2.py param --para 100
# python test-script2.py param -n 100
# MyCommand Class
# It's Your parameter 100

# -----------------------------------------------------

@DBScritp.command
def testcommand(servername='HP'):
    print('Server %s on' % servername)
# python test-script2.py testcommand
# MyCommand Class
# Server HP on
# python test-script2.py testcommand --servername IBM
# Server IBM on

# -----------------------------------------------------

# 互動
from flask_script import prompt_bool

@DBScritp.command
def do_something():
    if prompt_bool("Are you sure create new database"):
        print('You say yes')
# python test-script2.py do_something
# MyCommand Class
# Are you sure create new database [n]: y
# You say yes

# -----------------------------------------------------

from flask_script import Shell

# Shell
# def _make_context():
#     return dict(app='flask app', db='127.0.0.1')
#     # return "do some thing"
# DBScritp.add_command("shell", Shell(make_context=_make_context))
# python test-script2.py shell
# MyCommand Class, use flask_script
# >>> app
# 'flask app'
# >>> db
# '127.0.0.1'
# >>>

@DBScritp.shell
def _make_context():
    return dict(app='app', db='db')
# -----------------------------------------------------

# 查看路徑
from flask_script.commands import ShowUrls
DBScritp.add_command('show', ShowUrls())
# Rule                     Endpoint
# ---------------------------------
# /static/<path:filename>  static
# -----------------------------------------------------

if __name__ == '__main__':
    DBScritp.run()