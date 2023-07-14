import requests
from bs4 import BeautifulSoup
from app.scraper.webscraper import WebScraper
from app.data.xml_impl.protocol_xml import ProtocolXML

def main():

    url = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/866354-866354?limit=10&noFilterSet=true"
    web_scraper = WebScraper()
    soup_docs = web_scraper.get_soup_documents(url)

    protocol = ProtocolXML(soup_docs[0])
    print(protocol)

    agenda_item = protocol.agenda_items[0]
    print(agenda_item)

    for speech in agenda_item.speeches:
        print("\n\n")
        for text in speech.text:
            print(text)


if __name__ == "__main__":
    main()
