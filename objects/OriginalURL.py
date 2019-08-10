from random_words import RandomWords
import uuid
import datetime

from pymongo import MongoClient
from objects.DBClient import DBClient

class OriginalURL(MongoClient):

    def __init__(self, url):
        self.id = str(uuid.uuid4())
        self.url = url
        self.phrase = None

    def create_funny_phrase(self):

        phrase = ''

        rw = RandomWords()
        random_words = rw.random_words(count=3)

        for word in random_words:
            word = word.capitalize()
            phrase = phrase + word

        self.phrase = phrase

        return phrase

    def write_generated_phrase_to_db(self):

        if self.does_url_already_exist():
            print(f"The url {self.url} already exists in the database. Can't write dublicate")

        else:
            data = {
                    "_id":self.id,
                    "url":self.url,
                    "phrase":self.phrase,
                    "date": datetime.datetime.now()
            }

            try:
                db_client = DBClient()
                write = db_client.collection.insert_one(data)

            except Exception as e:
                print(e)

            if write.acknowledged:
                print(f"{write.inserted_id}: The url {self.url} has been inserted into database with phrases {self.phrase}")
            else:
                print(f"Could not write the url: {self.url} to database.")

    def does_url_already_exist(self):

        try:
            db_client = DBClient()
            result = db_client.collection.count(
                {"url":self.url}
            )

        except Exception as e:
            print (e)

        if result == 0:
            return False
        elif result != 0:
            return True

    def does_phrase_already_exist(self):
        pass


