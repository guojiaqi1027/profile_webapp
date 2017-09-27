import json
from flask import Blueprint, request
from src.action.authentication import token_required
from src.action.profile.profile_action import update_user_profile
from src.action.response.respons_action import token_ret
from src.action.profile import get_profile_by_uid_action
from src.action.profile import profile_action


profile_api = Blueprint('profile_api', __name__, url_prefix='/profile_api')

@profile_api.route('/update_profile', methods=['GET', 'POST'])
@token_required
def update_profile(uid, token):
    profile = json.loads(request.values.get('profile'))
    ret = update_user_profile(uid, profile)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)

@profile_api.route('/get_profile', methods=['GET', 'POST'])
@token_required
def get_profile(uid, token):
    profile = get_profile_by_uid_action(uid)
    return token_ret(token=token, success=1, profile=profile)
