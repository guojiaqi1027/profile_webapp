class MongoConfig:
    DB_NAME = 'profile_app'

class MongoLocalConfig(MongoConfig):
    ENTRY_POINT = '127.0.0.1',
    PORT = '27017',


MONGO_CONFIG = MongoLocalConfig()