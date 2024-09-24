from flask import Blueprint

laptops = Blueprint('laptops', __name__, template_folder='templates_laptops')

from . import routes, forms
