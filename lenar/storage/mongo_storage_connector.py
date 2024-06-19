from typing import List
from pymongo import MongoClient
from storage.storage_connector import StorageConnector


class MongoStorageConnector(StorageConnector):

    def __init__(self, client: MongoClient, db_name: str):
        super(MongoStorageConnector, self).__init__(client)
        self.db = self.client[db_name]

    def close(self):
        self.client.close()

    def find(self, collection_name: str) -> List[dict]:
        return list(self.db[collection_name].find(limit=100))

    def insert_one(self, collection_name: str, document: dict) -> dict:
        document.pop('_id', None)
        document['_id'] = self.db[collection_name].insert_one(document).inserted_id
        return document
