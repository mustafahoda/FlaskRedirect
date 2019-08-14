from objects.DBClient import DBClient

class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase
        self.url = None

    def get_url(self):
        db_client = DBClient()
        query = {'phrase' : self.phrase}
        query_result = db_client.collection.find_one(query)

        result = query_result['url']


        result = 'http://' + result
        return result