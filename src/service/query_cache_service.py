from src.cache import token_redis_client
from src.utils import generate_token

def get_uid_by_token(token):
    token = token_redis_client.get_user_uid(token)
    return token


def create_token_for_uid(uid):
    token = generate_token()
    token_redis_client.set_user_token(uid=str(uid), token=token)
    return token