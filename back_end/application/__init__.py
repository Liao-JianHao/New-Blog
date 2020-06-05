from flask import Flask
from flask_session import Session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy


from settings.dev import DevelopmentConfig
from settings.prop import ProductionConfig


config = {
    "dev": DevelopmentConfig,
    "prop": ProductionConfig,
}

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    config_obj = config[config_name]
    app.config.from_object(config_obj)

    CSRFProtect(app)
    Session(app)

    db.init_app(app)
    from .apps import main
    app.register_blueprint(main, url_prefix="")  # 注册main蓝图对象

    return app