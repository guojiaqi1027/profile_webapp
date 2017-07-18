from configs import REDIS_CONFIG
from cache import redis_client
class TokenRedisClient:
    def __init__(self, client):
      self.client = client


    def get_user_uid(self, token):
      return self.client.get_value(token)


    def set_user_token(self, uid, token):
      self.client.set_value(value=uid, key=token, expire=REDIS_CONFIG.DEFAULT_EXPIRE)


token_redis_client = TokenRedisClient(redis_client)
