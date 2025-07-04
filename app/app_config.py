
import os

class AppConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'sqlalchemy'
    SESSION_USE_SIGNER = True

class DevelopmentConfig(AppConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SECRET_KEY = 'dev-secret-key'

class ProductionConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///prod.db').replace("postgres://", "postgresql://", 1)
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'prod-secret-key')
