from bs4 import BeautifulSoup
from backend.app.data.xml_impl.protocol_xml import ProtocolXML
from backend.app.scraper.webscraper import WebScraper
from backend.app.data.xml_impl.faction_xml import FactionXML
from backend.app.data.xml_impl.speaker_xml import SpeakerXML
from backend.app.utils.utils import compute_hash, beuatify_string
from backend.app.data.db_impl.speech_db import SpeechDB
from backend.app.data.db_impl.speaker_db import SpeakerDB
from backend.app.data.db_impl.protocol_db import ProtocolDB


class Factory:
    """
    A factory to create and manage various XML and DB entities such as protocols, speakers, factions, etc.

    @ivar protocols: List of parsed protocols.
    @ivar speakers: Dictionary of speakers parsed from XML.
    @ivar speakers_db: Dictionary of speaker objects to be stored in the database.
    @ivar factions: Dictionary of factions.
    @ivar db: Database connection instance.
    """
    
    def __init__(self, database, xml = False):
        """
        Initialize the Factory with a given database. Optionally, initializes XML parsing.

        @param database: The database connection instance.
        @param xml: Boolean indicating whether to initialize XML parsing.
        """
        self.protocols = []
        self.speakers = {}
        self.speakers_db = {}
        self.factions = {}
        self.db = database
        if xml:
            self.init()
            

    def init(self):
        """
        Initiates the parsing of protocols.
        """
        self._parse_protocols()


    def _parse_protocols(self):
        """
        Retrieves soup documents and then processes them to create protocol objects.
        """
        soup_docs = self._get_soup_documents()
        print(f"Parsing {len(soup_docs)} soup documents ...")
        for soup_doc in soup_docs:
            _ = self._create_protocol(soup_doc)
            

    def _get_soup_documents(self) -> list:
        """
        Uses the web scraper to fetch soup documents.

        @return: List of soup documents.
        """
        web_scraper = WebScraper()
        soup_docs = web_scraper.get_soup_documents()
        return soup_docs


    def _create_protocol(self, soup_document : BeautifulSoup) -> ProtocolXML:
        """
        Creates a protocol from a given soup document and appends it to the protocols list.

        @param soup_document: The soup document to process.
        @return: The created ProtocolXML object.
        """
        protocol = ProtocolXML(soup_document, self)
        self.protocols.append(protocol)
        print(f"Number of agenda items: {len(protocol.agenda_items)}")
        print(f"Number of speeches: {sum([len(agenda_item.speeches) for agenda_item in protocol.agenda_items])}")
        print(f"Number of comments: {sum([len(speech.comments) for agenda_item in protocol.agenda_items for speech in agenda_item.speeches])}")
        print("Protocol parsed!")
        return protocol
    

    def get_faction(self, name, speaker):
        """
        Fetches a faction by its name or creates one if it doesn't exist. Also adds a speaker to the faction.

        @param name: Name of the faction.
        @param speaker: The speaker to be added to the faction.
        @return: The FactionXML object.
        """
        id = compute_hash(name)
        if id in self.factions:
            self.factions[id].add_speaker(speaker)
            return self.factions[id]
            
        faction = FactionXML(id, name)
        faction.add_speaker(speaker)
        self.factions[id] = faction
        
        return faction
    
        
    def get_speaker(self, xml, speech):
        """
        Fetches a speaker from the XML data or creates a new one if not found. Also associates a speech with the speaker.

        @param xml: XML data containing speaker information.
        @param speech: The speech to be associated with the speaker.
        @return: The SpeakerXML object.
        """
        name = xml.find("name")
        if name.find("vorname") is not None or name.find("nachname") is not None:

            last_name = beuatify_string(name.find("nachname").get_text())
            first_name = beuatify_string(name.find("vorname").get_text())

            id = compute_hash(first_name + last_name)
        else:
            id = compute_hash(name.get_text())
            first_name = name.get_text()
            last_name = name.get_text()
        
        if id in self.speakers:
            self.speakers[id].add_speech(speech)
            return self.speakers[id]
        
        speaker = SpeakerXML(xml, self, id, first_name, last_name)
        speaker.add_speech(speech)
        self.speakers[id] = speaker
        
        return speaker
