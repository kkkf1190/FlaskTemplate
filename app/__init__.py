##程序工厂函数
from flask import Flask,render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.wtf import Form
from config import config

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    #蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app