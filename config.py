import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'A-VERY-LONG-SECRET-KEY'

    # RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_OPTIONS = {'theme': 'black'}

    RECAPTCHA_USE_SSL = False

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'USER_INFO.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
