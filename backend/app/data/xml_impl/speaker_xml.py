
from backend.app.utils.utils import beuatify_string, compute_hash

class SpeakerXML:
    """
    Represents a speaker parsed from XML data.

    @ivar document: The BeautifulSoup object containing the XML data for the speaker.
    @ivar id: Unique identifier for the speaker.
    @ivar title: Title associated with the speaker.
    @ivar name: Full name of the speaker, including the title if present.
    @ivar first_name: First name of the speaker.
    @ivar last_name: Last name of the speaker.
    @ivar role_long: Extended role description of the speaker.
    @ivar role_short: Shortened role description of the speaker.
    @ivar faction: Faction affiliation of the speaker.
    @ivar speeches: List of speeches associated with the speaker.
    @ivar factory: Reference to the associated Factory object.
    """
    def __init__(self, speaker_xml, factory, id, first_name, last_name):
        """
        Initializes a speaker with the given XML data and other parameters.

        @param speaker_xml: The BeautifulSoup object containing the XML data for the speaker.
        @param factory: Reference to the associated Factory object.
        @param id: Unique identifier for the speaker.
        @param first_name: First name of the speaker.
        @param last_name: Last name of the speaker.
        """
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
        """Parses the XML data to populate the speaker attributes."""
        self.parse_title()
        self.parse_name()
        self.parse_role()
        self.parse_faction()
        
        
    def parse_title(self):
        """Parses and sets the title of the speaker from the XML data."""
        title = self.document.find("titel")
        if title is None:
            self.title = None
            return
        self.title = beuatify_string(title.get_text())


    def parse_name(self):
        self.name = self.first_name + " " + self.last_name
        if self.title:
            self.name = self.title + " " + self.name
    
    def parse_role(self):
 
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
        """
        Adds a speech to the speaker's list of speeches.

        @param speech: Speech object to be added.
        """
        self.speeches.append(speech)

    def to_mongo(self):
        """
        Converts the speaker to its MongoDB representation.

        @return: A dictionary representing the MongoDB format of the speaker.
        """
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
        """Returns a string representation of the speaker."""
        return f"\nSpeaker: {self.name} \t {self.id} \t {self.faction} \t (speeches {len(self.speeches)})\n"
    
    def __eq__(self, __value: object) -> bool:
        """
        Compares two speakers for equality based on their IDs.

        @param __value: The other speaker to compare with.
        @return: True if both speakers are equal, False otherwise.
        """
        if not isinstance(__value, SpeakerXML):
            return False
        return self.id == __value.id