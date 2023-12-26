from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)

# 設定 Flask app 的配置，用於郵件設定
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = '應用程式密碼'
app.config['MAIL_DEFAULT_SENDER'] = 'email@example.com'

mail = Mail(app)

@app.route('/')
def index():
    return 'Welcome to Flask Mail Example!'

@app.route('/send_mail')
def send_mail():
    try:
        # 建立郵件內容
        message = Message(subject='Hello from Flask-Mail',
                          recipients=['email@gmail.com'],   # 收件者
                          cc=['cc_recipient@example.com'],  # 副本 (CC)
                          bcc=['bcc_recipient@example.com'],  # 密件副本 (BCC)
                          sender=('Your Name', 'email@gmail.com'),  # 寄件人
                          reply_to='email@gmail.com',  # 回覆地址
                          body='This is a test email sent from Flask-Mail.')

        # 夾帶檔案
        # with app.open_resource("path/to/attachment.txt") as attachment:
        #     message.attach("attachment.txt", "text/plain", attachment.read())

        # 寄送郵件
        mail.send(message)
        print(message)
        flash('Email sent successfully!', 'success')
    except Exception as e:
        flash(f'Error sending email: {str(e)}', 'danger')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'your-secret-key'
    app.run(debug=True)