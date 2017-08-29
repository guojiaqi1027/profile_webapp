from src.service import query_db_service
from authentication_action import create_authentication_for_uid
import datetime, re
from src.action.profile.profile_action import get_profile_by_uid_action
def signup(credential, profile):
    ret = validate_credential(credential)
    if ret.get('code') < 0:
        return ret

    ret = validate_profile(profile)
    if ret.get('code') < 0:
        return ret

    uid = insert_signup_to_db(credential, profile)
    token_ret = create_authentication_for_uid(uid)
    token = token_ret['token']
    profile = get_profile_by_uid_action(uid)
    ret = {
        'token': token,
        'uid': uid
    }
    return ret


def validate_credential(credential):
    username = credential.get('username')
    password = credential.get('password')
    if not username or not password:
        ret = {
            'code': -201,
            'msg': 'Parameter error, username or password cannot be empty'
        }
        return ret

    if len(username) < 5:
        ret = {
            'code': -202,
            'msg': 'Parameter error, username is less than 5 characters'
        }
        return ret

    if len(password) < 7:
        ret = {
            'code': -203,
            'msg': 'Parameter error, password is less than 7 characters'
        }
        return ret

    filter = {
        'username': username
    }
    doc = query_db_service.query_user_credential(filter)

    if len(doc) == 0:
        ret = {
            'code': 1
        }
        return ret

    else:
        ret = {
            'code': -204,
            'msg': 'Username exist'
        }
        return ret

def validate_profile(profile):
    name = profile.get('name')
    title = profile.get('title')
    company = profile.get('company')
    address = profile.get('address')
    birth = profile.get('birth')
    email = profile.get('email')
    phone = profile.get('phone')

    if birth:
        try:
            datetime.datetime.strptime(birth, '%Y-%m-%d')
        except ValueError:
            ret = {
                'code': -205,
                'msg': 'Birth date invalid'
            }
            return ret

    if email and not re.match('.+\@.+\..+', email):
        ret = {
            'code': -206,
            'msg': 'Email format invalid'
        }
        return ret

    if phone and not re.match('^1(3|4|5|7|8)\d{9}$', phone):
        ret = {
            'code': -207,
            'msg': 'Phone number format invalid'
        }
        return ret

    ret = {
        'code': 1
    }
    return ret

def insert_signup_to_db(credential, profile):
    uid = query_db_service.vending_id('uid')
    credential['uid'] = uid
    profile['uid'] = uid
    query_db_service.insert_user_credential(credential)
    query_db_service.insert_user_profile(profile)
    return uid
