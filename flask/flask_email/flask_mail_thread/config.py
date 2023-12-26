import os
from dotenv import load_dotenv
load_dotenv()

# ENV = 'development'
DEBUG = True

MAIL_SERVER = os.getenv('MAIL_SERVER')
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = MAIL_USERNAME


