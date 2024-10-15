from flask import Blueprint

laptops = Blueprint('laptops', __name__, template_folder='templates')

from . import routes, forms
