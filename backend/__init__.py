from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
from backend.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
session = Session()
login_manager = LoginManager()
login_manager.login_view = 'admin.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    session.init_app(app)
    login_manager.init_app(app)

    from backend.captive_portal.routes import captive
    from backend.admin.routes import admin
    from backend.errors.handlers import errors

    app.register_blueprint(captive)
    app.register_blueprint(admin)
    app.register_blueprint(errors)

    return app


