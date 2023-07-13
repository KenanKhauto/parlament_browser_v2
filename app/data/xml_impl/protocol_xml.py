from bs4 import BeautifulSoup
from app.data.xml_impl.agenda_item_xml import AgendaItemXML

class ProtocolXML:

    def __init__(self, soup_document : BeautifulSoup):
        self.document = soup_document
        self.date = None
        self.agenda_items = []
        self.session_start = None
        self.session_end = None
        self.session_duration = None
        self.session_number = None
        self.session_title = None
        self.legislative_period = None
        self.parse()

    def parse(self):
        self.parse_date()
        self.parse_session_start()
        self.parse_session_end()
        self.parse_session_duration()
        self.parse_session_number()
        self.parse_session_title()
        self.parse_legislative_period()
        self.parse_agenda_items()

    def parse_legislative_period(self):
        legislative_period = self.document.find("dbtplenarprotokoll").get("wahlperiode")
        if legislative_period is None:
            self.legislative_period = "Unknown"
        else:
            self.legislative_period = legislative_period
    
    def parse_date(self):
        date = self.document.find("dbtplenarprotokoll").get("sitzung-datum")
        if date is None:
            self.data = "Unknown"
        else:
            self.date = date

    def parse_session_start(self):
        session_start = self.document.find("dbtplenarprotokoll").get("sitzung-start-uhrzeit")
        if session_start is None:
            self.session_start = "Unknown"
        else:
            self.session_start = session_start

    def parse_session_end(self):
        session_end = self.document.find("dbtplenarprotokoll").get("sitzung-ende-uhrzeit")
        if session_end is None:
            self.session_end = "Unknown"
        else:
            self.session_end = session_end

    
    def parse_session_duration(self):
        pass
    
    def parse_session_number(self):
        session_number = self.document.find("dbtplenarprotokoll").get("sitzung-nr")
        if session_number is None:
            raise Exception("Session number not found")
        self.session_number = session_number

    def parse_session_title(self):
        self.session_title = f"Sitzung {self.session_number}"

    def parse_agenda_items(self):
        agenda_items_docs = self.document.find_all("tagesordnungspunkt")
        for agenda_item in agenda_items_docs:
            agenda_item_xml = AgendaItemXML(agenda_item)
            self.agenda_items.append(agenda_item_xml)
        

    def __str__(self):
        return f"Protokoll [{self.legislative_period}]: {self.date} \t {self.session_title}"
    
    def to_mongo(self):
        return {
            "date": self.date,
            "session_start": self.session_start,
            "session_end": self.session_end,
            "session_duration": self.session_duration,
            "session_number": self.session_number,
            "session_title": self.session_title,
            "legislative_period": self.legislative_period,
            "agenda_items": [agenda_item.to_mongo() for agenda_item in self.agenda_items]
        }