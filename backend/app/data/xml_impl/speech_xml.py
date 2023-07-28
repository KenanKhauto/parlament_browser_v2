
from bs4 import BeautifulSoup

class SpeechXML:
    """
    Represents a speech parsed from XML data.

    @ivar document: The BeautifulSoup object containing the XML data for the speech.
    @ivar agenda_item: Associated agenda item for the speech.
    @ivar id: Unique identifier for the speech.
    @ivar speaker: SpeakerXML object who delivered the speech.
    @ivar date: Date of the speech.
    @ivar comments: List of comments associated with the speech.
    @ivar text: Text content of the speech.
    @ivar factory: Reference to the associated Factory object.
    @ivar legislative_period: Legislative period during which the speech was delivered.
    @ivar protocol: ProtocolXML object containing the speech.
    """

    def __init__(self, speech_xml: BeautifulSoup, agenda_item):
        """
        Initializes a speech with the given XML data and associated agenda item.

        @param speech_xml: The BeautifulSoup object containing the XML data for the speech.
        @param agenda_item: Associated agenda item for the speech.
        """
        self.document = speech_xml
        self.agenda_item = agenda_item
        self.id = None
        self.speaker = None
        self.date = self.agenda_item.protocol.date
        self.comments = []
        self.text = []
        self.factory = self.agenda_item.factory
        self.legislative_period = self.agenda_item.protocol.legislative_period
        self.protocol = self.agenda_item.protocol
        self.parse()


    def parse(self):
        """Parses the XML data to populate the speech attributes."""
        self.parse_speaker()
        self.parse_comments()
        self.parse_id()
        self.parse_text()


    def parse_text(self):
        text_elements = self.document.find_all("p", {"klasse": "J"})
        if text_elements is None:
            self.text = []
            return
        for element in text_elements:
            self.text.append(element.get_text())

    
    def parse_id(self):
        self.id = self.document.get("id")


    def parse_speaker(self):
        self.speaker_xml = self.document.find("redner")
        self.speaker = self.factory.get_speaker(self.speaker_xml, self)


    def parse_comments(self):

        comments = self.document.find_all("kommentar")
        if comments is None:
            self.comments = []
            return
        for comment in comments:
            self.comments.append(comment.get_text())
     

    def __eq__(self, __value: object) -> bool:
        """
        Compares two speeches for equality based on their IDs.

        @param __value: The other speech to compare with.
        @return: True if both speeches are equal, False otherwise.
        """
        if not isinstance(__value, SpeechXML):
            return False
        return self.id == __value.id


    def __str__(self) -> str:
        """Returns a string representation of the speech."""
        return f"\nSpeech: {self.id} num comments {len(self.comments)} \t {self.date} \n"


    def to_mongo(self):
        """
        Converts the speech to its MongoDB representation.

        @return: A dictionary representing the MongoDB format of the speech.
        """
        return {
            "_id": self.id,
            "protocol": self.protocol.id,
            "speaker": self.speaker.id,
            "legislative_period": self.legislative_period,
            "date": self.date,
            "comments": self.comments,
            "text": self.text,
            "agenda_item": self.agenda_item.id
        }