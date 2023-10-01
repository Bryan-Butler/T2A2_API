import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import app_config
import sqlalchemy as sa

bcrypt = Bcrypt()
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

def init_app():
    # load environment variable
    from dotenv import load_dotenv
    load_dotenv()

    # create flask app instance
    app = Flask(__name__)

    # app configuration
    app.config.from_object(app_config)
    jwt.init_app(app)

    # connect to D
    db.init_app(app)

    # connect schemas
    ma.init_app(app)

    # connect CLI commands 
    from commands import db_commands
    app.register_blueprint(db_commands)

  
    #connect blueprint controllers
    from controllers import all_controllers

    for controller in all_controllers:
        app.register_blueprint(controller)

    return app