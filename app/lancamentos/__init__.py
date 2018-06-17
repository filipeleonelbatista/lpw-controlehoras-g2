from flask import Blueprint
lancamentos = Blueprint('lancamentos', __name__)  # type: Blueprint
from . import routes
