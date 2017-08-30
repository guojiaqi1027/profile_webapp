import json
from flask import Blueprint, request
from src.action.summary import summary_action
from src.action.authentication import token_required
from src.action.response.respons_action import failure_ret, token_ret

summary_api = Blueprint('summary_api', __name__, url_prefix='/summary_api')

@summary_api.route('/get_summary', methods=['GET', 'POST'])
@token_required
def get_summary(uid, token):
    summary = summary_action.get_sumamry_by_uid_action(uid)
    return token_ret(token=token, success=1, summary=summary)


@summary_api.route('/update_summary', methods=['GET', 'POST'])
@token_required
def update_summary(uid, token):
    summary = request.values.get('summary')
    ret = summary_action.update_user_summary(uid, summary)
    code = ret.get('code', 1)
    if code < 0:
        msg = ret.get('msg')
        return token_ret(token=token, code=code, success=0, msg=msg)
    else:
        return token_ret(token=token, ret=ret)
