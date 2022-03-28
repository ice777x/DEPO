import requests
from bs4 import BeautifulSoup

class Crawl():
    def __init__(self,url):
        self.url = url
        self.url_list = list(self.url)
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
        next_navigation = "https://www.google.com"+soup.select("td a#pnnext")[0]['href']
        self.url_list.append(next_navigation)

    def crawl(self):
        for i in self.url_list:
            soup = self.connect(i)
            self.next_navigation(soup)
        return self.url_list
url = "https://www.google.com/search?q=werwer"
c = Crawl(url)
z = c.crawl()
print(z)
