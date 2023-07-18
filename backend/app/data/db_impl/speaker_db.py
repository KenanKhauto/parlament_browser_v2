
class SpeakerDB:

    def __init__(self, mongo_doc) -> None:
        
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.title = self.document["title"]
        self.name = self.document["name"]
        self.first_name = self.document["first_name"]
        self.last_name = self.document["last_name"]
        self.role_long = self.document["role_long"]
        self.role_short = self.document["role_short"]
        self.faction = self.document["faction"]
        self.speeches = self.document["speeches"]

    def add_speech(self, speech):
        self.speeches.append(speech)

    def to_json(self):
        return self.document