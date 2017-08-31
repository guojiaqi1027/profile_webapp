import json
from flask import Blueprint, request
from src.action.authentication import token_required
from src.action.education import education_action
from src.action.response.respons_action import token_ret


education_api = Blueprint('education_api', __name__, url_prefix='/education_api')

@education_api.route('/insert_education', methods=['GET', 'POST'])
@token_required
def insert_education(uid, token):
    education = json.loads(request.values.get('education'))
    ret = education_action.insert_education(uid, education)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)


@education_api.route('/get_educations', methods=['GET', 'POST'])
@token_required
def get_educations(uid, token):
    educations = education_action.get_educations_by_uid(uid)
    return token_ret(token=token, educations=educations)


@education_api.route('/delete_education', methods=['GET', 'POST'])
@token_required
def delete_education(uid, token):
    education_id = request.values.get('education_id')
    ret = education_action.delete_education(education_id)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)


@education_api.route('/update_education', methods=['GET', 'POST'])
@token_required
def update_education(uid, token):
    education = json.loads(request.values.get('education'))
    education_id = request.values.get('education_id')
    ret = education_action.update_education(education_id, education)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)
