import json
from flask import Blueprint, request
from src.service import query_db_service, query_cache_service
from src.action.response.respons_action import jsonify, failure_ret, token_ret
from src.action.authentication import authentication_action, token_required, signup
from src.action.profile import get_profile_by_uid_action 


public_api = Blueprint('public_api', __name__, url_prefix='/public_api')


@public_api.route('/get_user_profile', methods=['GET', 'POST'])
@token_required
def get_user_profile():
    uid = request.values.get('uid')
    uid = int(uid)
    profile = get_profile_by_uid_action(uid)
    return jsonify(profile=profile, success=1)


@public_api.route('/get_user_uid_from_token')
@token_required
def get_user_uid_from_token():
    token = request.values.get('token')
    uid = query_cache_service.get_uid_by_token(token)
    return jsonify(uid=uid, token=token, success=1)


@public_api.route('/generate_token_for_uid')
def generate_token_for_uid():
    uid = request.values.get('uid')
    token = query_cache_service.create_token_for_uid(uid)
    return jsonify(uid=uid, token=token, success=1)


@public_api.route('/authentication', methods=['GET', 'POST'])
def authentication():
    username = request.values.get('username')
    password = request.values.get('password')
    if not username or not password:
        return failure_ret(code=-100, msg="Missing Parameters")
    ret = authentication_action(username, password)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return failure_ret(code=code, msg=msg)
    else:
        token = ret.get('token')
        return token_ret(token=token, ret=ret, success=1)


@public_api.route('/signup', methods=['POST'])
def user_signup():
    credential_raw = json.loads(request.values.get('credential'))
    profile = json.loads(request.values.get('profile'))

    if not credential_raw or not profile:
        return failure_ret(code=-200, msg='Parameter error, credential or profile can not be empty')

    credential = {
        'username': credential_raw.get('username'),
        'password': credential_raw.get('password')
    }

    ret = signup(credential, profile)
    code = ret.get('code')
    if code < 0:
        return failure_ret(code=code, msg=ret.get('msg'))
    else:
        token = ret.get('token')
        return token_ret(token=token, ret=ret, success=1)
