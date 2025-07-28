from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from app.app_config import DevelopmentConfig, ProductionConfig
from app.blueprint import blueprint

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app(config_name="development"):
    app = Flask(__name__)

    if config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(blueprint)

    return app
