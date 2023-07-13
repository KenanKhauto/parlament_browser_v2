import requests
from bs4 import BeautifulSoup
from app.scraper.webscraper import WebScraper

def main():
    api_key = "?api_key=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF"
    url = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/866354-866354?limit=10&noFilterSet=true"
    web_scraper = WebScraper()
    soup_docs = web_scraper.get_soup_documents(url)
    # get the first soup document
    soup_doc = soup_docs[0]
    # get the first agenda item
    agenda_item = soup_doc.find('tagesordnungspunkt', recursive=True)
    file_path = 'output.xml'
    agenda_item_path = 'agenda_item.xml'
    # Write the XML content to the file
    with open(file_path, 'w') as file:
        file.write(str(soup_doc))
    with open(agenda_item_path, 'w') as file:
        file.write(str(agenda_item))






    

if __name__ == "__main__":
    main()


'''
 import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

class Protocol:
    def __init__(self, url):
        self.url = url
        self.agenda_items = []

    def parse(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract XML content using Jsoup
        xml_content = str(soup.select('selector-for-xml-element')[0])  # Adjust the selector for the XML element
        
        # Parse XML content using ElementTree
        root = ET.fromstring(xml_content)

        # Parse agenda items
        agenda_nodes = root.findall('agendaitem')
        for agenda_node in agenda_nodes:
            agenda_item = AgendaItem(agenda_node)
            self.agenda_items.append(agenda_item)

class AgendaItem:
    def __init__(self, node):
        self.node = node
        self.speeches = []

    def parse(self):
        # Parse speeches within the agenda item
        speech_nodes = self.node.findall('speech')
        for speech_node in speech_nodes:
            speech = Speech(speech_node)
            self.speeches.append(speech)

class Speech:
    def __init__(self, node):
        self.node = node
        self.speaker = node.attrib.get('speaker')
        self.content = node.text

# Usage
protocol = Protocol('http://example.com/protocol-page')  # Replace with the actual URL of the page containing the XML
protocol.parse()

for agenda_item in protocol.agenda_items:
    print(f"Agenda Item ID: {agenda_item.node.attrib.get('id')}")
    for speech in agenda_item.speeches:
        print(f"Speaker: {speech.speaker}")
        print(f"Content: {speech.content}")
        print()
 
 '''   