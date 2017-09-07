from src.service import query_db_service
from src.utils import validator
import datetime


def get_educations_by_uid(uid):
    if not uid:
        return None
    filter = {
      'uid': uid
    }
    docs = query_db_service.query_user_educations(filter)
    return docs


def insert_education(uid, education):
    ret = validate_education(education)
    if ret.get('code') < 0:
        return ret

    education_id = query_db_service.vending_id('education_id')
    education['education_id'] = education_id
    education['uid'] = uid
    query_db_service.insert_user_education(education)
    return ret


def validate_education(education):
    start_t = education.get('start_t')
    end_t = education.get('end_t')
    ret = validator.start_end_validator(start_t, end_t)
    if ret['code'] < 0:
        return ret

    school = education.get('school')
    if not school:
        ret = {
            'code': -222,
            'msg': 'School is empty'
        }
        return ret

    major = education.get('major')
    if not major:
        ret = {
            'code': -223,
            'msg': 'Major is empty'
        }
        return ret

    ret = {
            'code': 1
    }
    return ret


def delete_education(education_id):
    filter = {
        'education_id': int(education_id)
    }
    query_db_service.delete_user_education(filter)
    ret = {
        'code': 1
    }
    return ret


def update_education(education_id, education):
    ret = validate_education(education)
    if ret.get('code') < 0:
        return ret

    filter = {
        'education_id': int(education_id)
    }
    query_db_service.update_user_education(filter, education)
    return ret
