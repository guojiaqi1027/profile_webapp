class MongoConfig:
    DB_NAME = 'profile_app'
    USER_CREDENTIAL_COLLECTION = 'user_credential'
    USER_PROFILE_COLLECTION = 'user_profile'
    SEQUENCE_COLLECTION = 'sequence'
    USER_SUMMARY_COLLECTION = 'user_summary'
    USER_EDUCATION_COLLECTION = 'user_education'
    USER_EXPERIENCE_COLLECTION = 'user_experience'


class MongoLocalConfig(MongoConfig):
    ENTRY_POINT = '127.0.0.1'
    PORT = 27017


MONGO_CONFIG = MongoLocalConfig()
