import requests
from bs4 import BeautifulSoup
import httpx
import asyncio
import json

url = "https://www.discudemy.com/language/Turkish"


class DiscUdemy:
    def __init__(self, url):
        self.url = url
        self.data = []
        self.links = []

    def discUdemy(self, soup):
        for i in soup.select("section.card"):
            dil = i.select("label.disc-fee")
            if dil[0].text.lower() == 'ads':
                continue
            link = i.select("a.card-header")[0]['href']
            self.links.append(
                f"https://discudemy.com/go/{link.split('/')[-1]}")
        title = i.select("a.card-header")[0].text
        self.data.append({"dil": dil[0].text, "title": title})
        return

    async def _getDiscLink(self):
        urls = [i for i in self.links]
        async with httpx.AsyncClient() as client:
            tasks = (client.get(url) for url in urls)
            req2 = await asyncio.gather(*tasks)

        htmls = [rq2.content for rq2 in req2]
        for index, html in enumerate(htmls):
            sup = BeautifulSoup(html, 'html.parser')
            link = sup.select("a.couponLink")[0].text
            self.data[index]["link"] = link
        return

    async def main(self):
        r = requests.get(self.url)
        s = BeautifulSoup(r.content, 'html.parser')
        urls = [self.url+"/" +
                str(i) for i in range(1, int(s.select("ul.pagination3 li a")[-2].text)+1)]
        async with httpx.AsyncClient() as client:
            tasks = (client.get(url) for url in urls)
            re = await asyncio.gather(*tasks)

        htmls = [req.content for req in re]

        data = []
        for html in htmls:
            soupS = BeautifulSoup(html, 'html.parser')
            self.discUdemy(soupS)

        return

    def getDisc(self):
        asyncio.run(self._getDiscLink)

    def export_data(self):
        self.getDisc()
        with open("discUdemy.json", "w") as f:
            json.dump(self.data, f, ensure_ascii=True,
                      sort_keys=True, indent=2)


d1 = DiscUdemy(url)
d1.export_data()
