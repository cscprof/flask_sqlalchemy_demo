from flask import Blueprint

vehicles = Blueprint('vehicles', __name__, template_folder='templates_vehicles')

from . import routes
