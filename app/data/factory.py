from bs4 import BeautifulSoup
from app.data.xml_impl.protocol_xml import ProtocolXML
from app.scraper.webscraper import WebScraper
from app.data.xml_impl.faction_xml import FactionXML
from app.data.xml_impl.speaker_xml import SpeakerXML
from app.utils.utils import compute_hash, beuatify_string
from app.data.db_impl.speech_db import SpeechDB
from app.data.db_impl.speaker_db import SpeakerDB
from app.data.db_impl.protocol_db import ProtocolDB


class Factory:
    
    def __init__(self, database, xml = False):
        self.protocols = []
        self.speakers = {}
        self.speakers_db = {}
        self.factions = {}
        self.db = database
        if xml:
            self.init()
            

    def init(self):
        self._parse_protocols()

    def _parse_protocols(self):
        soup_docs = self._get_soup_documents()
        print(f"Parsing {len(soup_docs)} soup documents ...")
        for soup_doc in soup_docs:
            _ = self._create_protocol(soup_doc)
            

    def _get_soup_documents(self) -> list:
        web_scraper = WebScraper()
        soup_docs = web_scraper.get_soup_documents()
        return soup_docs

    def _create_protocol(self, soup_document : BeautifulSoup) -> ProtocolXML:
        protocol = ProtocolXML(soup_document, self)
        self.protocols.append(protocol)
        print(f"Number of agenda items: {len(protocol.agenda_items)}")
        print(f"Number of speeches: {sum([len(agenda_item.speeches) for agenda_item in protocol.agenda_items])}")
        print(f"Number of comments: {sum([len(speech.comments) for agenda_item in protocol.agenda_items for speech in agenda_item.speeches])}")
        print("Protocol parsed!")
        return protocol
    

    def get_faction(self, name, speaker):
        
        id = compute_hash(name)
        if id in self.factions:
            self.factions[id].add_speaker(speaker)
            return self.factions[id]
            
        faction = FactionXML(id, name)
        faction.add_speaker(speaker)
        self.factions[id] = faction
        
        return faction
    
        
    def get_speaker(self, xml, speech):

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
