import requests
from bs4 import BeautifulSoup


class WebScraper:

    def __init__(self) -> None:
        self.MAIN_URL = "https://www.bundestag.de"

    def get_xml_links(self, url: str) -> list:
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')
        xml_links = soup.select('a[href$=".xml"]')
        return xml_links
    
    def get_xml_content(self, url: str) -> str:
        xml_response = requests.get(url)
        xml_content = xml_response.text
        return xml_content
    
    def get_xml_soup(self, url: str) -> BeautifulSoup:
        xml_content = self.get_xml_content(self.MAIN_URL + url)
        xml_soup = BeautifulSoup(xml_content, "lxml")
        return xml_soup
    
    def get_xml_after_pagination(self, url: str):
        all_xml_links = []
        offset = 0
        while True:
            new_url = url + "&offset=" + str(offset)
            xml_links = self.get_xml_links(new_url)
            if len(xml_links) == 0:
                break
            all_xml_links += xml_links
            offset += 10
            print(f"extracted {len(xml_links)} links from {new_url}")
        print(f"total links extracted: {len(all_xml_links)}")

        return all_xml_links
    
    def get_soup_documents(self, url: str) -> list[BeautifulSoup]:
        xml_links = self.get_xml_after_pagination(url)
        soup_documents = []
        for i, xml_link in enumerate(xml_links):
            soup_document = self.get_xml_soup(xml_link['href'])
            soup_documents.append(soup_document)
            print(f"extracted soup document {i+1} of {len(xml_links)}")
        return soup_documents