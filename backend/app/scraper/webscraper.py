import requests
from bs4 import BeautifulSoup


class WebScraper:
    """
    A web scraper designed to extract XML links and content from the Bundestag website.

    @ivar MAIN_URL: The main URL of the Bundestag website.
    @ivar ajax_url1: AJAX URL for specific filtering.
    @ivar ajax_url2: Another AJAX URL for specific filtering.
    """

    def __init__(self) -> None:
        """
        Initializes the WebScraper with default URLs.
        """
        self.MAIN_URL = "https://www.bundestag.de"
        self.ajax_url1 = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/866354-866354?limit=10&noFilterSet=true" #20
        self.ajax_url2 = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/543410-543410?limit=10&noFilterSet=true" #19


    def get_xml_links(self, url: str) -> list:
        """
        Fetches and extracts XML links from a given URL.

        @param url: The URL from which XML links should be extracted.
        @return: A list containing XML links.
        """
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content)
        xml_links = soup.select('a[href$=".xml"]')
        return xml_links
    

    def get_xml_content(self, url: str) -> str:
        """
        Fetches XML content from a given URL.

        @param url: The URL from which the XML content should be fetched.
        @return: A string containing the XML content.
        """
        xml_response = requests.get(url)
        xml_content = xml_response.text
        return xml_content
    

    def get_xml_soup(self, url: str) -> BeautifulSoup:
        """
        Fetches XML content and parses it into a BeautifulSoup object.

        @param url: The XML URL to fetch and parse.
        @return: A BeautifulSoup object containing the parsed XML content.
        """
        xml_content = self.get_xml_content(self.MAIN_URL + url)
        xml_soup = BeautifulSoup(xml_content, "lxml")
        return xml_soup


    def get_xml_after_pagination(self, url: str):
        """
        Continuously fetches and extracts XML links from a URL with pagination.

        @param url: The base URL with potential paginated XML links.
        @return: A list containing all XML links from all pages.
        """
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
    
    
    def get_soup_documents(self) -> list[BeautifulSoup]:
        """
        Fetches and parses XML documents from two specific AJAX URLs.

        @return: A list of BeautifulSoup objects, each containing parsed XML content from the fetched links.
        """
        xml_links = self.get_xml_after_pagination(self.ajax_url1)
        xml_links += self.get_xml_after_pagination(self.ajax_url2)
        soup_documents = []
        for i, xml_link in enumerate(xml_links):
            soup_document = self.get_xml_soup(xml_link['href'])
            soup_documents.append(soup_document)
            print(f"extracted soup document {i+1} of {len(xml_links)}")
        return soup_documents