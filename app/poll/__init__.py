from flask import Blueprint

poll = Blueprint('poll', __name__)

from app.poll import routes