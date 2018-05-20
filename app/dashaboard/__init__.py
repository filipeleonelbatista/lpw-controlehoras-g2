from flask import Blueprint
dashaboard = Blueprint('dashaboard', __name__)
from . import routes, routesht, routeshxp
