from flask import Flask, jsonify
from flask_restful import Api
from flask_swagger import swagger
from models import db
from controllers import UserController
import json

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Swagger UI
from flask_swagger_ui import get_swaggerui_blueprint

# 設定 Swagger UI 的路徑
SWAGGER_URL = '/api/docs'
# 設定 Swagger JSON 的路徑
API_URL = '/swagger'

# 設定 Swagger UI 的配置
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'My API',
    }
)
# 將 Swagger UI 的 Blueprint 加入到 Flask 應用程式中
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

api = Api(app)
api.add_resource(UserController, '/users', '/users/<int:user_id>')

# 新增 Swagger 文檔路由
@app.route("/swagger")
def swagger_spec():
    swag = swagger(app, from_file_keyword='swagger_from_file')
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'My API'
    swag['basePath'] = '/'
    swag['host'] = 'localhost:5000'
    swag['schemes'] = ['http']

    # 將 Swagger 輸出成 JSON 檔案
    with open('swagger.json', 'w') as f:
        json.dump(swag, f)

    return jsonify(swag)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)