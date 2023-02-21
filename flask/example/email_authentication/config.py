import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    pjdir = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
                 os.path.join(pjdir, 'app_blog/static/data/data_register.sqlite')
    SECRET_KEY = b'\xe6\x9c\x8b\xe5\x8f\x8b'
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PROT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')