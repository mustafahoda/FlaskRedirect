from pymongo import MongoClient

client = MongoClient()

class DB():
    def __init__(self):
        self.db = client.URLphrases