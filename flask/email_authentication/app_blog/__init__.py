from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import Config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)
bootstrap = Bootstrap(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#  很重要，一定要放這邊
from app_blog.author import view