import requests
from bs4 import BeautifulSoup
from app.scraper.webscraper import WebScraper
from app.data.xml_impl.protocol import Protocol

def main():
    api_key = "?api_key=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF"
    url = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/866354-866354?limit=10&noFilterSet=true"
    web_scraper = WebScraper()
    soup_docs = web_scraper.get_soup_documents(url)
    # get the first soup document
    print("-----------------------------------------")
    for soup_doc in soup_docs:
        protocol = Protocol(soup_doc)
        print(protocol.date)
        print(protocol.session_start)
        print(protocol.session_end)
        print(protocol.session_number)
        print(protocol.session_title)
        print("_____________________________")







    

if __name__ == "__main__":
    main()


'''
 from bs4 import BeautifulSoup

class Protocol:
    def __init__(self):
        self.agenda_items = []

    def add_agenda_item(self, agenda_item):
        self.agenda_items.append(agenda_item)

    def __str__(self):
        return f"Protocol: {len(self.agenda_items)} agenda items"


class AgendaItem:
    def __init__(self, title):
        self.title = title
        self.speeches = []

    def add_speech(self, speech):
        self.speeches.append(speech)

    def __str__(self):
        return f"Agenda Item: {self.title}"


class Speech:
    def __init__(self, speaker, text):
        self.speaker = speaker
        self.text = text

    def __str__(self):
        return f"Speech by {self.speaker}: {self.text}"


# Example XML protocol
xml_string = 
<protocol>
    <agendaItem>
        <title>Item 1</title>
        <speech>
            <speaker>Speaker 1</speaker>
            <text>Speech 1</text>
        </speech>
        <speech>
            <speaker>Speaker 2</speaker>
            <text>Speech 2</text>
        </speech>
    </agendaItem>
    <agendaItem>
        <title>Item 2</title>
        <speech>
            <speaker>Speaker 3</speaker>
            <text>Speech 3</text>
        </speech>
    </agendaItem>
</protocol>


# Parse the XML protocol using BeautifulSoup
soup = BeautifulSoup(xml_string, 'xml')

# Create a Protocol object
protocol = Protocol()

# Extract agenda items and speeches from the XML
agenda_items = soup.find_all('agendaItem')

# Process each agenda item
for agenda_item in agenda_items:
    title = agenda_item.find('title').text
    item = AgendaItem(title)

    speeches = agenda_item.find_all('speech')
    # Process each speech within the agenda item
    for speech in speeches:
        speaker = speech.find('speaker').text
        text = speech.find('text').text
        item.add_speech(Speech(speaker, text))

    # Add the agenda item to the protocol
    protocol.add_agenda_item(item)

# Print the protocol structure
print(protocol)
for item in protocol.agenda_items:
    print(item)
    for speech in item.speeches:
        print(speech)
 
 '''   