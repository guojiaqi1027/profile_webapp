from flask import Blueprint, request
from src.action.summary import summary_action
from src.action.search import search_action
from src.action.authentication import token_required
from src.action.response.respons_action import failure_ret, token_ret

search_api = Blueprint('search_api', __name__, url_prefix='/search_api')

@search_api.route('/search', methods=['GET', 'POST'])
@token_required
def search(uid, token):
    keys = request.values.get('keys')
    keys = keys.lower()
    keys = keys.split('+')
    uids = search_action.get_all_uids()
    items = search_action.search_all_uids(keys, uids)
    return token_ret(items=items, token=token)
