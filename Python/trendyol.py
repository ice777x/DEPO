from bs4 import BeautifulSoup
import re
import asyncio
import requests
import aiohttp
from time import time
import json
import os


class Trendyol:

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    def __init__(self, url):
        self.url = url
        self.urls = self.get_urls()
        self.item_data = []
        self.BASE_URL = "https://www.trendyol.com"
        self.exportDict = {}
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }

    def get_urls(self):
        r = requests.get(self.url)
        text = r.text.split('class="dscrptn">')[1].split("</div>")[0]
        pattern = "\d+"
        item_adedi = int(re.findall(pattern, text)[-1])
        page_sayisi = item_adedi // 24
        urls = list((f"{self.url}&pi={i}" for i in range(1, page_sayisi+1)))
        return urls

    async def __get_data(self, url, session):
        async with session.get(url) as r:
            data = await r.text()
            return data

    async def __fetch(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            task = (asyncio.ensure_future(self.__get_data(url, session))
                    for url in self.urls)
            htmls = await asyncio.gather(*task)
            return htmls

    def __extract(self):
        link = list((self.BASE_URL + i.select("a")
                    [0]['href'] for i in self.item_data))
        title = list((i.select("span.prdct-desc-cntnr-name")
                      [0].text for i in self.item_data))
        price = list((i.select("div.prc-box-dscntd")
                      [0].text for i in self.item_data))
        x = 1
        for t, l, p in zip(title, link, price):
            self.exportDict[str(x)] = {"link": l,
                                       'title': t, 'price': p}
            x += 1

    def __scrape(self):
        try:
            htmls = asyncio.run(self.__fetch())
        except:
            print("zort")
            return
        for html in htmls:
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.select("div.p-card-wrppr")
            self.item_data.extend(items)
        self.__extract()
        return len(self.exportDict)

    @property
    def parse(self) -> dict:
        print(len(self.urls))
        return self.__scrape()

    def exportToJson(self):
        """parse ->> trendyol.json"""
        if os.path.exists("./trendyol.json"):
            os.remove("./trendyol.json")
        self.parse
        with open("trendyol.json", "w", encoding="utf-8") as file:
            json.dump(self.exportDict, file, ensure_ascii=True, indent=2)
        return "Exported trenyol.json in this directory"


url = "https://www.trendyol.com/sr?q=pull%20bear"
T = Trendyol(url)
# print(T.parse)
