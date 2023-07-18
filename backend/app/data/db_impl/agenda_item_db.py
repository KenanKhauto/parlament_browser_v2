

class AgendaItemDB:

    def __init__(self, mongo_document, protocol):
        self.document = mongo_document
        self.id = self.document["_id"]
        self.protocol = protocol
        self.title = self.document["title"]
        self.speeches_ids = self.document["speeches"]
        self.table_of_contents = self.document["table_of_contents"]
        self.speeches = self.document["speeches"]

    def to_json(self):
        return self.document