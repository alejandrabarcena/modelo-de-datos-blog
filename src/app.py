import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from .models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)

    db_url = os.getenv("DATABASE_URL")
    if db_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = db_url.replace("postgres://", "postgresql://")
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    with app.app_context():
        from . import models  # registra modelos

    @app.get("/health")
    def health():
        return jsonify(ok=True)

    return app

app = create_app()
