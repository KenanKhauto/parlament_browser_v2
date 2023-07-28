from bs4 import BeautifulSoup
from backend.app.data.xml_impl.speech_xml import SpeechXML
from backend.app.utils.utils import compute_hash

class AgendaItemXML:
    """
    Represents an agenda item parsed from XML data.

    @ivar document: The BeautifulSoup document representing the agenda item.
    @ivar id: Unique identifier for the agenda item.
    @ivar title: The title of the agenda item.
    @ivar table_of_contents: List of table of contents for the agenda item.
    @ivar speeches: List of speeches associated with the agenda item.
    @ivar protocol: The protocol to which the agenda item belongs.
    @ivar factory: The factory instance used for parsing and object creation.
    """
    def __init__(self, soup_document : BeautifulSoup, protocol):
        """
        Initializes an agenda item from the given BeautifulSoup document and protocol.

        @param soup_document: The BeautifulSoup document representing the agenda item.
        @param protocol: The protocol to which the agenda item belongs.
        """
        self.document = soup_document
        self.id = None
        self.title = None
        self.table_of_contents = []
        self.speeches = []
        self.protocol = protocol
        self.factory = protocol.factory
        self.parse()


    def parse(self):
        """
        Triggers the parsing of the agenda item.
        """
        self.parse_title()
        self.create_unique_id()
        self.parse_table_of_contents()
        self.parse_speeches()


    def create_unique_id(self):
        """
        Generates a unique ID for the agenda item based on its title.
        """
        if self.title is None:
            self.id = None
            return
        self.id = compute_hash(self.title)
 

    def parse_title(self):
        """
        Extracts the title of the agenda item from the document.
        """
        try:
            self.title = self.document.get("top-id")
        except:
            self.title = None
            print("Could not parse title")


    def parse_table_of_contents(self):
        """
        Extracts the table of contents associated with the agenda item from the document.
        """
        contents = self.document.find_all("p", {"klasse": "T_NaS"})
        if contents is None:
            self.table_of_contents = []
            return
        for content in contents:
            if content.get_text() not in self.table_of_contents:
                self.table_of_contents.append(content.get_text())
    

    def parse_speeches(self):
        """
        Extracts and parses the speeches associated with the agenda item from the document.
        """
        speeches = self.document.find_all("rede")
        if speeches is None:
            self.speeches = []
            return
        for speech in speeches:
            self.speeches.append(SpeechXML(speech, self))


    def to_mongo(self):
        """
        Converts the agenda item to its MongoDB representation.

        @return: A dictionary representing the MongoDB format of the agenda item.
        """
        return {
            "_id": self.id,
            "title": self.title,
            "table_of_contents": self.table_of_contents,
            "speeches": [speech.id for speech in self.speeches],
            "protocol_id": self.protocol.id
        }


    def __str__(self) -> str:
        """
        Returns a string representation of the agenda item.

        @return: A string representation.
        """
        return f"\nAgenda Item: {self.title} \t {self.id} \n"


    def __eq__(self, __value: object) -> bool:
        """
        Compares two agenda items for equality based on their IDs.

        @param __value: The other agenda item to compare with.
        @return: True if both items are equal, False otherwise.
        """
        if not isinstance(__value, AgendaItemXML):
            return False
        return self.id == __value.id
    
