from mongodb_client import mongodb_client
from configs.mongo_config import MONGO_CONFIG

class MongoDBDao:
    def __init__(self, mongodb_client, collection):
        self.client = mongodb_client
        self.collection = mongodb_client.get_collection(collection)


    def fetch_single_doc(self, filter, projection={'_id': False}):
        doc = self.collection.find_one(filter, projection)
        if not doc:
            doc = dict()
        return doc


    def fetch_batch_docs(self, filter, projection={'_id': False}):
        pass


    def insert_single_doc(self, doc):
        self.collection.insert_one(doc)


    def update_single_doc(self, filter, doc):
        update = { '$set': doc }
        self.collection.update_one(filter, update)


user_credential_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.USER_CREDENTIAL_COLLECTION)
user_profile_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.USER_PROFILE_COLLECTION)
seq_dao = MongoDBDao(mongodb_client, MONGO_CONFIG.SEQUENCE_COLLECTION)
