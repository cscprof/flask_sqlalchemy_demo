'''
This file will configure application parameters used elsewhere
in the application. It will also allow us to select from multiple
configurations if we ever have a need to do so.

The config class will read the configuration values from the
settings.conf file.
'''

import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Read the application configuration file
import configparser
config = configparser.ConfigParser()
config.read('settings.conf')


class Config:
    SECRET_KEY = config["DEFAULT"]["SECRET_KEY"]
    SESSION_PERMANENT = config["SESSION"]["SESSION_PERMANENT"]
    SESSION_TYPE = config["SESSION"]["SESSION_TYPE"]

    @staticmethod
    def init_app(app):
        pass

# Configuration for Development
class BaseConfig(Config):
    DEBUG=True
    # SQLALCHEMY_DATABASE_URI = config["SQLALCHEMY"]["CONN_STRING"]
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://" + config["MYSQL"]["DB_USER"] + ":" + config["MYSQL"]["DB_PASSWORD"] + "@" + config["MYSQL"]["DB_HOST"] + ":" + config["MYSQL"]["DB_PORT"] + "/" + config["MYSQL"]["DB_DATABASE"]
    SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY"]["TRACK_MODIFICATIONS"]

# Configuration for Production Deployment
class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://" + config["MYSQL"]["DB_USER"] + ":" + config["MYSQL"]["DB_PASSWORD"] + "@" + config["MYSQL"]["DB_HOST"] + ":" + config["MYSQL"]["DB_PORT"] + "/" + config["MYSQL"]["DB_DATABASE"]
    SQLALCHEMY_TRACK_MODIFICATIONS = config["SQLALCHEMY"]["TRACK_MODIFICATIONS"]
    
config = {
    'base': BaseConfig,
    'production': ProductionConfig,
    'default': BaseConfig
}