

class SpeechDB:
    
    def __init__(self, mongo_doc) -> None:
        
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.text = self.document["text"]
        self.speaker = self.document["speaker"]
        self.agenda_item = self.document["agenda_item"]
        self.comments = self.document["comments"]
        self.leghislative_period = self.document
        self.date = self.document["date"]

        
    def to_json(self):
        return self.document