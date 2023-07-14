
from bs4 import BeautifulSoup

class SpeechXML:
    """
    This class is used to create the XML file for the speech.
    """

    def __init__(self, speech_xml: BeautifulSoup, agenda_item):
        """
        This method initializes the class.
        :param speech: The speech.
        """
        self.document = speech_xml
        self.agent_item = agenda_item
        self.id = None
        self.speaker = None
        self.date = self.agent_item.protocol.date
        self.comments = []
        self.text = []
        self.parse()

    def parse(self):
        """
        This method parses the speech.
        """
        self.parse_speaker()
        self.parse_comments()
        self.parse_id()
        self.parse_text()

    def parse_text(self):
        """
        This method parses the text.
        """
        text_elements = self.document.find_all("p", {"klasse": "J"})
        if text_elements is None:
            self.text = []
            return
        for element in text_elements:
            self.text.append(element.get_text())

    
    def parse_id(self):
        """
        This method parses the id.
        """
        self.id = self.document.get("id")
    
    def parse_speaker(self):
        """
        This method parses the speaker.
        """
        
        self.speaker_xml = self.document.find("redner")
        #TODO: parse speaker

    def parse_comments(self):
        """
        This method parses the comments.
        """
        comments = self.document.find_all("kommentar")
        if comments is None:
            self.comments = []
            return
        for comment in comments:
            self.comments.append(comment.get_text())
     
    def __eq__(self, __value: object) -> bool:
        """
        This method checks if two objects are equal.
        :param __value: The object to compare.
        :return: True if the objects are equal, False otherwise.
        """
        if not isinstance(__value, SpeechXML):
            return False
        return self.id == __value.id


    def __str__(self) -> str:
        """
        This method returns the string representation of the object.
        :return: The string representation of the object.
        """
        return f"\nSpeech: {self.id} num comments {len(self.comments)} \t {self.date} \n"

    def to_mongo(self):
        """
        This method returns the object as a mongo object.
        :return: The object as a mongo object.
        """
        return {
            "_id": self.id,
            "speaker": self.speaker.id,
            "date": self.date,
            "comments": self.comments,
            "text": self.text,
            "agenda_item": self.agent_item.id
        }