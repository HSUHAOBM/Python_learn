from flask import Flask, redirect, request, url_for, session
import requests
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# LINE Notify OAuth2 設定
# https://notify-bot.line.me/my/services/ 註冊應用後取得 client ID 和 client secret
LINE_NOTIFY_CLIENT_ID = 'xxxxxxxxxxx'
LINE_NOTIFY_CLIENT_SECRET = 'xxxxxxxxxxxxxxxx'
LINE_NOTIFY_REDIRECT_URI = 'https://b330-211-75-231-148.ngrok-free.app/callback'
LINE_NOTIFY_AUTH_URL = 'https://notify-bot.line.me/oauth/authorize'
LINE_NOTIFY_TOKEN_URL = 'https://notify-bot.line.me/oauth/token'
LINE_NOTIFY_SCOPE = 'notify'


# Step 1: 引導使用者到 LINE Notify 授權頁面，並選擇「1 對 1 聊天」
@app.route('/')
def index():
    auth_url = (
        f"{LINE_NOTIFY_AUTH_URL}?response_type=code&client_id={LINE_NOTIFY_CLIENT_ID}"
        f"&redirect_uri={LINE_NOTIFY_REDIRECT_URI}&scope={LINE_NOTIFY_SCOPE}&state=your_csrf_token"
    )
    return redirect(auth_url)


# Step 2: 授權後回調，處理 LINE 傳回的 authorization code
# 當用戶授權後，LINE 會將用戶重定向到此路由，並附帶授權碼
# 舉例 /callback?code=QhIz38ZiyZ7y3arBLC2oIU&state=your_csrf_token
@app.route('/callback')
def callback():
    code = request.args.get('code')
    state = request.args.get('state')

    # Step 3: 使用 authorization code 換取 access token 暫存 session，實務上存DB
    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': LINE_NOTIFY_REDIRECT_URI,
        'client_id': LINE_NOTIFY_CLIENT_ID,
        'client_secret': LINE_NOTIFY_CLIENT_SECRET,
    }

    token_response = requests.post(LINE_NOTIFY_TOKEN_URL, data=token_data)
    token_json = token_response.json()

    if 'access_token' in token_json:
        session['access_token'] = token_json['access_token']
        return "LINE Notify 綁定成功！"
    else:
        return "授權失敗", 400


# Step 4: 使用 access token 發送通知
@app.route('/notify')
def notify():
    access_token = session.get('access_token')
    print(f"access_token: {access_token}")
    if not access_token:
        return redirect(url_for('index'))

    message = "這是來自 Flask 的測試通知"
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    data = {
        'message': message
    }
    response = requests.post(
        'https://notify-api.line.me/api/notify', headers=headers, data=data)

    if response.status_code == 200:
        return "通知發送成功"
    else:
        return "通知發送失敗", 400


if __name__ == '__main__':
    app.run(debug=True)
