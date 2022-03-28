import requests
from bs4 import BeautifulSoup

class Crawl():
    def __init__(self,query):
        self.url = "https://www.google.com/search?q="+ query
        self.url_list = [self.url]
    def connect(self,url):
        r = requests.get(
                url,
                headers={
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
                },
            )
        soup = BeautifulSoup(r.content, "html.parser")
        return soup
    
    def next_navigation(self,soup):
        try:
            next_navigation = "https://www.google.com"+soup.select("td a#pnnext")[0]['href']
        except:
            return
        self.url_list.append(next_navigation)

    def crawl(self):
        for i in self.url_list:
            soup = self.connect(i)
            self.next_navigation(soup)
        return self.url_list
