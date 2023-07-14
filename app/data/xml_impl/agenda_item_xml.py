from bs4 import BeautifulSoup
from app.data.xml_impl.speech_xml import SpeechXML
from app.utils.utils import compute_hash

class AgendaItemXML:
    def __init__(self, soup_document : BeautifulSoup):
        self.document = soup_document
        print(f"Agenda item created!")
        self.id = None
        self.title = None
        self.table_of_contents = []
        self.speeches = []
        self.parse()

    def parse(self):
        self.parse_title()
        self.create_unique_id()
        self.parse_table_of_contents()
        self.parse_speeches()

    def create_unique_id(self):
        if self.title is None:
            self.id = None
            return
        self.id = compute_hash(self.title)
 
    def parse_title(self):
        try:
            self.title = self.document.get("top-id")
        except:
            self.title = None
            print("Could not parse title")

    def parse_table_of_contents(self):
        contents = self.document.find_all("p", {"klasse": "T_NaS"})
        if contents is None:
            self.table_of_contents = []
            return
        for content in contents:
            if content.get_text() not in self.table_of_contents:
                self.table_of_contents.append(content.get_text())
    
    def parse_speeches(self):
        speeches = self.document.find_all("rede")
        if speeches is None:
            self.speeches = []
            return
        for speech in speeches:
            self.speeches.append(SpeechXML(speech))


    def __str__(self) -> str:
        return f"\nAgenda Item: {self.title} \t {self.id} \n"
    
    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, AgendaItemXML):
            return False
        return self.id == __value.id
    