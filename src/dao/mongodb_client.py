from pymongo import MongoClient
from src.configs.mongo_config import MONGO_CONFIG

class MongoDBClient:


    def __init__(self, db_entry_point, db_port, db_name):
        self.mongo_client = MongoClient(db_entry_point, db_port)
        self.db = self.mongo_client[db_name]   


    def get_collection(self, collection):
        collection = self.db[collection]
        return collection


mongodb_client = MongoDBClient(MONGO_CONFIG.ENTRY_POINT,
                            MONGO_CONFIG.PORT,
                            MONGO_CONFIG.DB_NAME)
