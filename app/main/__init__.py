from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates_main')

from . import routes  # , forms
