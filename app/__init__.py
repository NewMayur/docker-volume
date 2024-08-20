from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'instance', 'messages.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully.")

    from app import routes
    app.register_blueprint(routes.main)

    return app