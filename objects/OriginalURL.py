from random_words import RandomWords
import uuid
import datetime

from objects.DB import DB

class OriginalURL(DB):

    def __init__(self, url):
        self.id = uuid.uuid4()
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
        data = {
                "url":self.url,
                "phrase":self.phrase,
                "date": datetime.datetime.now()
        }

        db = DB()
        db.db.phrase.insert_one(data).inserted_id

        print(f"{self.id}: The url {self.url} has been inserted into database with phrases {self.phrase}")
