from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)

    # Check if the tables exist before creating them
    with app.app_context():
        db.create_all()

    from app import routes
    app.register_blueprint(routes.main)

    return app