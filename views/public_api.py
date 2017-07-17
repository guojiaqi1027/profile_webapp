from flask import Blueprint, request
from service import query_db_service
from utils import jsonify

public_api = Blueprint('public_api', __name__, url_prefix='/public_api')


@public_api.route('/get_user_profile')
def get_user_profile():
    uid = request.values.get('uid')
    uid = int(uid)
    profile = query_db_service.query_user_profile(uid)
    return jsonify(profile=profile, success=1)
