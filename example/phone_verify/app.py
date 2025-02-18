from flask import Flask, render_template, request, session,jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 設定 Twilio 相關參數
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
service_sid = os.getenv("service_sid")

client = Client(account_sid, auth_token)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    # 取得表單提交的 JSON 格式資料
    data = request.get_json()
    # 從 JSON 資料中取得手機號碼
    phone_number = data['phone_number']

    try:
        # # 創建 Verify service
        # service = client.verify.services.create(friendly_name='my-verification-service')
        # 發送驗證碼
        verification = client.verify \
                            .services(service_sid) \
                            .verifications \
                            .create(to=phone_number, channel='sms')

        # 儲存相關資訊到 session
        session['phone_number'] = phone_number

        if verification.status == 'pending':
            return jsonify({'result': True, 'msg' : 'sent ok'})

    except TwilioRestException as e:
        return jsonify({'result': False, 'msg': str(e) })

@app.route('/check_verification', methods=['POST'])
def check_verification():

    data = request.get_json()
    verification_code = data['verification_code']

    try:
        # 驗證驗證碼
        verification_check = client.verify \
                                   .services(service_sid) \
                                   .verification_checks \
                                   .create(to=session['phone_number'], code=verification_code)
        # 檢查驗證狀態，
        if verification_check.status == 'approved':
            return jsonify({'result': True, 'msg' : 'sent ok'})
        else:
            return jsonify({'result' : False, 'msg' : '驗證失敗'})

    except TwilioRestException as e:
        return jsonify({'result' : False, 'msg' : str(e)})

if __name__ == '__main__':
    app.run(debug=True)