from flask import Blueprint

public_api = Blueprint('public_api', __name__)


@public_api.route('/get_user_profile')
def get_user_profile():
    pass