import requests
from bs4 import BeautifulSoup

def main():
    api_key = "?api_key=rgsaY4U.oZRQKUHdJhF9qguHMkwCGIoLaqEcaHjYLF"
    url = "https://www.bundestag.de/ajax/filterlist/de/services/opendata/866354-866354?limit=10&noFilterSet=true&offset=0"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    xml_links = soup.select('a[href$=".xml"]')
    link = "https://www.bundestag.de" + xml_links[3]["href"]
    xml_response = requests.get(link)
    xml_content = xml_response.text
    xml_soup = BeautifulSoup(xml_content, "lxml")
    print(xml_soup.select("plenarprotokoll-nummer"))
    #for link in xml_links:
    #    xml_url = link['href']
    #    xml_response = requests.get("https://www.bundestag.de"+xml_url)
    #    xml_content = xml_response.text
    #    print(xml_content)

if __name__ == "__main__":
    main()