# Import the database
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from flask import Flask
from config import config


# Create the app instance
app = Flask(__name__)

# Define the app configuration
config_name = 'default'

# Get configuration data from settings.conf via the config class
app.config.from_object(config[config_name])
config[config_name].init_app(app)

# Initialize the databse connection
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

Session = sessionmaker(bind=engine)
session = Session()

# Create the Model prerequisites
Base = declarative_base()
