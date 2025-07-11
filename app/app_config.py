
import os

class AppConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'sqlalchemy'
    SESSION_USE_SIGNER = True
    TIMEZONE = 'Africa/Johannesburg'
    SMS_EXPIRY_MINS = 60
    WASTE_MANAGEMENT_PROVIDER_NAME = 'Untum'
    ADMIN_INITIAL_PASSWORD = 'admin123'
    BAG_SIZES = [5, 10, 20, 25 , 50 , 1000 ]
    MATERIAL_TYPES = ['LD Plastic', 'Glass', 'Cans', 'Cardboard', 'Paper', 'PET', 'HD', 'Common', 'Carton']
    PHOTO_WIDTH = 800


class DevelopmentConfig(AppConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    SECRET_KEY = 'dev-secret-key'

class ProductionConfig(AppConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///prod.db').replace("postgres://", "postgresql://", 1)
    SECRET_KEY = os.environ.get('FLASK_SECRET', 'prod-secret-key')
