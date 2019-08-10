from pymongo import MongoClient

client = MongoClient()

class DBClient():
    def __init__(self):
        self.client = client
        self.database = self.client.URLphrases
        self.collection = self.database.phrases