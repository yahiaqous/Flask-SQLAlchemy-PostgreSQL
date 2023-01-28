from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import config

# ----------------------------------------------- #

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_mode):
    app = Flask(__name__)
    app.config.from_object(config[config_mode])
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app

# ----------------------------------------------- #

# Migrate Commands:
    # flask db init
    # flask db migrate
    # flask db upgrade
    # ERROR [flask_migrate] Error: Can't locate revision identified by 'ID' => flask db revision --rev-id ID
    