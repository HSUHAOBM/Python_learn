from flask import Flask
from flask_restful import Api
from models import db
from controllers import UserController

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)
api.add_resource(UserController, '/users', '/users/<int:user_id>')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)