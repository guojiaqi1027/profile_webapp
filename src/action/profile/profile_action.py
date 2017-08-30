from src.service import query_db_service
import re, datetime

def get_profile_by_uid_action(uid):
    if not uid:
        return None

    filter = {
      'uid': uid
    }
    doc = query_db_service.query_user_profile(filter)
    return doc


def update_user_profile(uid, profile):
    ret = validate_profile(profile)
    if ret.get('code') < 0:
        return ret
    
    filter = {
      'uid': uid
    }
    query_db_service.update_user_profile(filter, profile)
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