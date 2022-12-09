from flask_mail import Mail, Message
from flask import Flask, request, make_response, render_template, url_for, redirect, Response
import config
from markupsafe import escape
from werkzeug.exceptions import HTTPException
import json
from threading import Thread

app = Flask(__name__)
app.config.from_object(config)

# 使用 flask_mail
mail = Mail(app)

@app.route('/mail', methods=['GET', 'POST'])
def send_mail():
    if request.method == 'GET':
        response = make_response(render_template('mail.html'))
    elif request.method == 'POST':

        # 收件人
        recipient = request.values.get('recipient', None)
        # 標題
        title = request.values.get('title', '')
        # 內容
        content = request.values.get('content', '')

        # 製作信件
        msg = Message(title, recipients=[recipient])
        msg.body = content

        # 使用非同步送出信件
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()

        response = make_response('Success')

    return response

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


@app.errorhandler(Exception)
def handle_exception(e):
    code = 500
    if isinstance(e, HTTPException):
        # print( 'IS HTTPException')
        code = e.code
    return Response(json.dumps(
        {"error": True, "code": code, "error_message": str(e)}, sort_keys=False), mimetype='application/json'), code

