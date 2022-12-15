
一對多 多對多關聯

flask_migrate 資料庫板控
export FLASK_APP=model.py
flask db init
flask db migrate -m "說明文字"
flask db upgrade
flask db stamp head
flask db --help
flask db downgrade
flask db history

參考
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships
https://hackmd.io/AfOvUnDaQMajup-OCXtmNg