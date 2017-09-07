import re, datetime
def email_validator(email):
    if re.match('.+\@.+\..+', email):
        ret = {
            'code': -300,
            'msg': 'Email format invalid'
        }
    else:
        ret = {
            'code': 1
        }
    return ret

def date_validator(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        ret = {
            'code': 1
        }
    except ValueError:
        ret = {
            'code': -301,
            'msg': 'Date format invalid'
        }
    return ret


def phone_validator(phone):
    if re.match('^1(3|4|5|7|8)\d{9}$', phone):
        ret = {
            'code': -302,
            'msg': 'Phone format invalid'
        }
    else:
        ret = {
            'code': 1
        }
    return ret


def start_end_validator(start_t, end_t):
    ret = date_validator(start_t)
    now = datetime.datetime.now()
    if ret['code'] < 0:
        return ret
    start_t = datetime.datetime.strptime(start_t, '%Y-%m-%d')
    if start_t > datetime.datetime.now():
        ret = {
          'code': -303,
          'msg': 'Start time later than now'
        }
        return ret

    if end_t != 'present':
        ret = date_validator(end_t)
        if ret['code'] < 0:
            return ret
        end_t = datetime.datetime.strptime(end_t, '%Y-%m-%d')
        if start_t >= end_t :
            ret = {
                'code': -304,
                'msg': 'Start time is later than end time'
            }
            return ret
        if end_t > now:
            ret = {
                'code': -305,
                'msg': 'End time later than now'
            }
            return ret
      
    ret = {
        'code': 1
    }
    return ret