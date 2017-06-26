from pymongo import MongoClient
from configs.mongo_config import MONGO_CONFIG

class MongoDBDao:


    def __init__(self, db_entry_point, db_port, db_name):
        self.mongo_client = MongoClient()
        self.db = mongo_client[db]


    def get_single_object(filter, collection):
        collection = self.db[collection]
        pass


    def get_batch_objects(filter, collection):
        collection = self.db[collection]
        pass


mongodb_dao = MongoDBDao(MONGO_CONFIG.ENTRY_POINT,
                            MONGO_CONFIG.PORT,
                            MONGO_CONFIG.DB_NAME)