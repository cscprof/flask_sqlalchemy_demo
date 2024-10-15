'''
This file creates the Flask application when you launch the
application with the

    python wsgi.py

command from the command prompt.

Each module (vehicles, customers, vendors, laptops, etc.) will
be added to the application here.

Helpful tutorial: 

    https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

'''
# Create an instance of the app, read in the configration
# Create the database connection and session
from app.extensions import app

def create_app():
    
    # From here onward we will add the functionality defined by the
    # individual Blueprints.  As new capabilities are added to the
    # application, new blueprints will be created and added here.

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'


    # Load the laptops functions
    from .laptops import laptops as laptops_blueprint
    app.register_blueprint(laptops_blueprint)

    # Load the vehicle functions
    from .vehicles import vehicles as vehicles_blueprint
    app.register_blueprint(vehicles_blueprint)

    # Load the laptops functions
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


