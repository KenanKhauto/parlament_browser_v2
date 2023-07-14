from bs4 import BeautifulSoup
from app.data.xml_impl.protocol_xml import ProtocolXML
from app.scraper.webscraper import WebScraper


class Factory:
    
    def __init__(self):
        self.protocols = []
        self.speakers = []
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
        protocol = ProtocolXML(soup_document)
        self.protocols.append(protocol)
        print(f"Number of agenda items: {len(protocol.agenda_items)}")
        print(f"Number of speeches: {sum([len(agenda_item.speeches) for agenda_item in protocol.agenda_items])}")
        print(f"Number of comments: {sum([len(speech.comments) for agenda_item in protocol.agenda_items for speech in agenda_item.speeches])}")
        print("Protocol parsed!")
        return protocol
    
