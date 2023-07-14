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

    for item in protocol.agenda_items:
        print(f"{item}")



if __name__ == "__main__":
    main()
