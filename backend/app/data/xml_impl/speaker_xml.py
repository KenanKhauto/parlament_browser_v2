
from backend.app.utils.utils import beuatify_string, compute_hash

class SpeakerXML:

    def __init__(self, speaker_xml, factory, id, first_name, last_name):

        self.document = speaker_xml
        self.id = id
        self.title = None
        self.name = None
        self.first_name = first_name
        self.last_name = last_name
        self.role_long = None
        self.role_short = None
        self.faction = None
        self.speeches = []
        self.factory = factory
        self.parse()

    def parse(self):
        """
        This method parses the speaker.
        """
        self.parse_title()
        self.parse_name()
        self.parse_role()
        self.parse_faction()
        
        
    def parse_title(self):
        """
        This method parses the title.
        """
        title = self.document.find("titel")
        if title is None:
            self.title = None
            return
        self.title = beuatify_string(title.get_text())


    def parse_name(self):
        """
        This method parses the name.
        """

        self.name = self.first_name + " " + self.last_name
        if self.title:
            self.name = self.title + " " + self.name
    
    def parse_role(self):
        """
        This method parses the role.
        """
        role = self.document.find("rolle")

        if role is None:
            self.role_long = None
            self.role_short = None
            return
        
        role_long = role.find("rolle_lang")
        role_short = role.find("rolle_kurz")
        if role_long is not None:
            self.role_long = beuatify_string(role_long.get_text())
        
        if role_short is not None:
            self.role_short = beuatify_string(role_short.get_text())


    def parse_faction(self):
        if self.document.find("fraktion") is not None:
            name = beuatify_string(self.document.find("fraktion").get_text())
            if name == "SPDCDU/CSU":
                name = "CDU/CSU"
            if name == "Fraktionslos":
                return
            self.faction = self.factory.get_faction(name, self)


    def add_speech(self, speech):
        self.speeches.append(speech)

    def to_mongo(self):
        return {
            "_id": self.id,
            "name": self.name,
            "title": self.title,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role_long": self.role_long,
            "role_short": self.role_short,
            "faction": self.faction.name if self.faction else None,
            "speeches": [speech.id for speech in self.speeches]
        }


    def __str__(self):
        return f"\nSpeaker: {self.name} \t {self.id} \t {self.faction} \t (speeches {len(self.speeches)})\n"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, SpeakerXML):
            return False
        return self.id == __value.id