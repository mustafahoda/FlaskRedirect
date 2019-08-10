from random_words import RandomWords
import uuid

class OriginalURL:

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
        pass