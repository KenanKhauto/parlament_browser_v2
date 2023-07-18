
class FactionDB:

    def __init__(self, mongo_doc) -> None:
        
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.name = self.document["name"]
        self.members = self.document["members"]

    