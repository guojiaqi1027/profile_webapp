from src.service import query_db_service
from src.utils import validator
import datetime


def get_experiences_by_uid(uid):
    if not uid:
        return None
    filter = {
      'uid': uid
    }
    docs = query_db_service.query_user_experiences(filter)
    return docs


def insert_experience(uid, experience):
    ret = validate_experience(experience)
    if ret.get('code') < 0:
        return ret

    experience_id = query_db_service.vending_id('experience_id')
    experience['experience_id'] = experience_id
    experience['uid'] = uid
    query_db_service.insert_user_experience(experience)
    return ret


def validate_experience(experience):
    start_t = experience.get('start_t')
    end_t = experience.get('end_t')
    ret = validator.start_end_validator(start_t, end_t)
    if ret['code'] < 0:
        return ret

    school = experience.get('company')
    if not school:
        ret = {
            'code': -222,
            'msg': 'Company is empty'
        }
        return ret

    major = experience.get('title')
    if not major:
        ret = {
            'code': -223,
            'msg': 'title is empty'
        }
        return ret

    ret = {
            'code': 1
    }
    return ret


def delete_experience(experience_id):
    filter = {
        'experience_id': int(experience_id)
    }
    query_db_service.delete_user_experience(filter)
    ret = {
        'code': 1
    }
    return ret


def update_experience(experience_id, experience):
    ret = validate_experience(experience)
    if ret.get('code') < 0:
        return ret

    filter = {
        'experience_id': int(experience_id)
    }
    query_db_service.update_user_experience(filter, experience)
    return ret
