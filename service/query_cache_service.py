from cache import token_redis_client


def get_uid_by_token(token):
    token = token_redis_client.get_user_uid(token)
    return token