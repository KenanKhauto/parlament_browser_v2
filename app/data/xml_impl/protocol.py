from bs4 import BeautifulSoup

'''

<dbtplenarprotokoll herausgeber="Deutscher Bundestag" 
herstellung="H. Heenemann GmbH  Co. KG, Buch- und Offsetdruckerei, Bessemerstraße 83–91, 12103 Berlin, www.heenemann-druck.de" 
issn="0722-7980" 
sitzung-datum="06.07.2023" 
sitzung-ende-uhrzeit="23:13" 
sitzung-naechste-datum="07.07.2023" 
sitzung-nr="115" sitzung-ort="Berlin" 
sitzung-start-uhrzeit="9:00" 
start-seitennr="14077" 
vertrieb="Bundesanzeiger Verlagsgesellschaft mbH, Postfach 1 0 05 34, 50445 Köln, Telefon (02 21) 97 66 83 40, Fax (02 21) 97 66 83 44, www.betrifft-gesetze.de" 
wahlperiode="20">
'''

class Protocol:

    def __init__(self, soup_document : BeautifulSoup):
        self.document = soup_document
        self.date = None
        self.agenda_items = []
        self.session_start = None
        self.session_end = None
        self.session_duration = None
        self.session_number = None
        self.session_title = None
        self.parse()

    def parse(self):
        self.parse_date()
        self.parse_session_start()
        self.parse_session_end()
        self.parse_session_duration()
        self.parse_session_number()
        self.parse_session_title()
    
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

    def add_agenda_item(self, agenda_item):
        self.agenda_items.append(agenda_item)

    def __str__(self):
        return f"Protocol: {self.date} \t {self.session_title}"
    