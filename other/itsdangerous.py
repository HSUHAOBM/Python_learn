# -*- coding:UTF-8 -*-

from itsdangerous import TimedJSONWebSignatureSerializer,BadSignature,SignatureExpired
import time
#  預設為3600秒
s = TimedJSONWebSignatureSerializer('YourKey', expires_in=3)
#  dumps 將密鑰與資料做序列化
token = s.dumps({'id': 1})

# time.sleep(4)

try:
    data = s.loads(token)  # 驗證
except SignatureExpired:
    #  時間超過
    print('SignatureExpired, over time')
except BadSignature:
    #  驗證錯誤的
    print('BadSignature, No match')
finally:
    print('finish')