from flask import Flask
from .models import db, init_db
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)

    app.register_blueprint(main)

    return app