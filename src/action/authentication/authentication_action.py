from src.service.query_db_service import query_user_credential
from src.service.query_cache_service import create_token_for_uid

def authentication_action(username, password):
    filter = {'username': username}
    doc = query_user_credential(filter)
    doc_password = doc.get('password')
    ret = dict()
    
    if not doc:
        ret['code'] = -102
        ret['msg'] = 'Authentication failed, username not found'
        return ret

    if doc_password != password:
        ret['code'] = -103
        ret['msg'] = 'Authentication failed, username and password not match'
        return ret

    else:
        uid = doc.get('uid')
        return create_autehntication_for_uid(uid)


def create_autehntication_for_uid(uid):
    if not uid:
        ret = {
            'code': -104,
            'msg': 'Token error, cannot get uid'
        }
        return ret
    token = create_token_for_uid(uid)
    ret = {
        'code': 1,
        'token': token
    }
    return ret
