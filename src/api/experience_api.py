import json
from flask import Blueprint, request
from src.action.authentication import token_required
from src.action.experience import experience_action
from src.action.response.respons_action import token_ret


experience_api = Blueprint('experience_api', __name__, url_prefix='/experience_api')

@experience_api.route('/insert_experience', methods=['GET', 'POST'])
@token_required
def insert_experience(uid, token):
    experience = json.loads(request.values.get('experience'))
    ret = experience_action.insert_experience(uid, experience)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)


@experience_api.route('/get_experiences', methods=['GET', 'POST'])
@token_required
def get_experiences(uid, token):
    experiences = experience_action.get_experiences_by_uid(uid)
    return token_ret(token=token, experiences=experiences)


@experience_api.route('/delete_experience', methods=['GET', 'POST'])
@token_required
def delete_experience(uid, token):
    experience_id = request.values.get('experience_id')
    ret = experience_action.delete_experience(experience_id)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)


@experience_api.route('/update_experience', methods=['GET', 'POST'])
@token_required
def update_experience(uid, token):
    experience = json.loads(request.values.get('experience'))
    experience_id = request.values.get('experience_id')
    ret = experience_action.update_experience(experience_id, experience)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)
