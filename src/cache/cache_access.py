import redis
from src.configs import REDIS_CONFIG

class RedisClient:
      def __init__(self, redis_entry_point, redis_port):
        self.client = redis.Redis(host=redis_entry_point, port=redis_port)

      def get_value(self, key):
        value = self.client.get(key)
        return value


      def set_value(self, key, value, expire=None):
        self.client.set(name=key,value=value,ex=expire);
        return


redis_client = RedisClient(REDIS_CONFIG.ENTRY_POINT, REDIS_CONFIG.PORT)