import functools
from flask import request
from src.utils import failure_ret
from src.service import query_cache_service


def token_required(func):
    """
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = request.values.get('token')
        if not token:
            return failure_ret(code=-100, msg='Token is missing')

        uid = query_cache_service.get_uid_by_token(token)
        if not uid:
            return failure_ret(code=-101, msg="Token is invalid")
        else:
            return func(*args, **kwargs)

    return wrapper
