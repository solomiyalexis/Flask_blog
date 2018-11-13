import os

class Config:
    SECRET_KEY = '4954d2f5eaa68f8c232a487dd16cde0d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get ('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get ('EMAIL_PASS')