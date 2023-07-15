


class FactionXML:

    def __init__(self, id, name):
            
            self.id = id
            self.name = name
            self.members = []
    
    def add_speaker(self, speaker):
        self.members.append(speaker)

    def to_mongo(self):
        return {
            "_id": self.id,
            "name": self.name,
            "members": [member.id for member in self.members]
        }
    
    def __str__(self) -> str:
        return f"{self.name} ({len(self.members)} members)"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, FactionXML):
            return False
        return self.id == __value.id
    