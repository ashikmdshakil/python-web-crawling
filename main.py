import requests
from bs4 import BeautifulSoup

def crawl_page(max_page):
    page = 1
    while(page <= max_page):
        url = 'https://www.startech.com.bd/component/ram?page='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, features="html.parser")
        for elem in soup.findAll('h4',{'class': 'p-item-name'}):
            link = elem.find('a')
            print(link.string)
        page += 1

crawl_page(1)