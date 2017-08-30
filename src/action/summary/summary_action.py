from src.service import query_db_service


def get_sumamry_by_uid_action(uid):
    if not uid:
        return None
    
    filter = {
      'uid': uid
    }
    count = query_db_service.count_user_summary(filter)
    if count == 0:
        return None
    else:
      doc = query_db_service.query_user_summary(filter)
      return doc['summary']


def update_user_summary(uid, summary):
    ret = validate_summary(summary)
    if ret.get('code') < 0:
        return ret
    
    filter = {
        'uid': uid
    }
    count = query_db_service.count_user_summary(filter)
    doc = {
        'uid': uid,
        'summary': summary
    }
    if count > 0:
        query_db_service.update_user_summary(filter, doc)
    else:
        query_db_service.insert_user_summary(doc)
    return ret


def validate_summary(summary):
    if summary and len(summary) < 200:
        ret = {
          'code': 1
        }
    else:
        ret = {
          'code': -210,
          'msg': 'Summary length should between 1 and 200'
        }
    return ret