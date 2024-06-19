from typing import List
from pymongo import MongoClient
from bson import ObjectId
from bson.errors import InvalidId
from storage.storage_connector import StorageConnector
from storage.exceptions import NotFound


def _mongo_id_str_converter(func):
    def wrapped(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result is None:
                return
            if isinstance(result, list):
                documents_dicts = result
            else:
                documents_dicts = [result]
            for d in documents_dicts:
                if "_id" in d:
                    d["_id"] = str(d.pop("_id"))
                if 'password' in d:
                    d['password'] = '*' * 8
            return result

        except InvalidId:  # raised when document_id in ObjectId(document_id) is not a valid document id value.
            raise NotFound()
    return wrapped


class MongoStorageConnector(StorageConnector):

    def __init__(self, client: MongoClient, db_name: str):
        super(MongoStorageConnector, self).__init__(client)
        self.db = self.client[db_name]

    def close(self):
        self.client.close()

    @_mongo_id_str_converter
    def find(self, collection_name: str) -> List[dict]:
        return list(self.db[collection_name].find(limit=100))

    def find_one(self, collection_name: str, document) -> dict:
        user = self.db[collection_name].find_one(document)
        if user is None:
            raise NotFound()
        return user

    @_mongo_id_str_converter
    def insert_one(self, collection_name: str, document: dict) -> dict:
        document.pop('_id', None)
        document['_id'] = self.db[collection_name].insert_one(document).inserted_id
        return document

    @_mongo_id_str_converter
    def update_one(self, collection_name: str, document_id: str, document: dict) -> dict:
        if 'password' in document and not document['password']:
            document.pop('password')
            
        stored_document = self.find_one(collection_name, {"_id": ObjectId(document_id)})
        # filter fields according to model
        stored_document.update(document)
        self.db[collection_name].update_one({"_id": ObjectId(document_id)}, {"$set": stored_document})
        return stored_document

    @_mongo_id_str_converter
    def delete_one(self, collection_name: str, document_id: str):
        delete_result = self.db[collection_name].delete_one({"_id": ObjectId(document_id)})
        if delete_result.deleted_count != 1:
            raise NotFound()

    @_mongo_id_str_converter
    def matches(self, collection_name: str, document: dict) -> bool:
        if '_id' in document:
            document['_id'] = ObjectId(document['_id'])
        return self.db[collection_name].find_one(document) is not None
