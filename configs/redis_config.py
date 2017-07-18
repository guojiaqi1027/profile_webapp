class RedisConfig:
    pass


class RedisLocalConfig(RedisConfig):
    ENTRY_POINT = '127.0.0.1'
    PORT = 6379
    DEFAULT_EXPIRE = 1800


REDIS_CONFIG = RedisLocalConfig()