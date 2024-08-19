from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    SQLALCHEMY_DATABASE_URI='sqlite:///instance/flaskr.sqlite',
)

db = SQLAlchemy(app)

from . import routes
app.register_blueprint(routes.bp)

def create_app():
    db.init_app(app)
    return app
