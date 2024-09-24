'''
This file creates the Flask application when you launch the
application with the

    python flasky.py

command from the command prompt.

Each module (vehicles, customers, vendors, laptops, etc.) will
be added to the application here.

Helpful tutorial: 

    https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

'''
import os
from flask import Flask
from config import config

# Import the database
from app.extensions import db

def create_app():
    app = Flask(__name__)

    config_name = 'default'

    # Get configuration data from settings.conf via the config class
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Initialize Flask extensions here
    db.init_app(app)

    # From here onward we will add the functionality defined by the
    # individual Blueprints.  As new capabilities are added to the
    # application, new blueprints will be created and added here.

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'


    # Load the laptops functions
    from .laptops import laptops as laptops_blueprint
    app.register_blueprint(laptops_blueprint)

    # Load the laptops functions
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

