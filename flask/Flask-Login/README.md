```
pip install flask-login
```

參考
https://github.com/maxcountryman/flask-login
https://hackmd.io/@shaoeChen/HJiZtEngG/https%3A%2F%2Fhackmd.io%2Fs%2Fryvr_ly8f
https://medium.com/seaniap/python-web-flask-flask-login%E7%99%BB%E5%85%A5%E7%B3%BB%E7%B5%B1%E5%AF%A6%E4%BD%9C-51c5ffda7924

is_authenticated
登入成功時return True(這時候才能過的了login_required)
is_active
帳號啟用並且登入成功的時候return True
is_anonymous
匿名用戶return True(登入用戶會return False)
get_id()
取得當前用戶id