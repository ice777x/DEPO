from bs4 import BeautifulSoup
import asyncio
import requests
import aiohttp


class CrawlSite:
    """>>>crawl = CrawlSite(url="https://github.com/search?q=python", selector=".next_page")"""

    def __init__(self, url, selector):
        self.selector = selector
        self.url = url
        self.url_list = [self.url]
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
        self.baseUrl = f"{self.url.split('/')[0]}//{self.url.split('/')[2]}"

    def __soup(self, url):
        r = requests.get(
            url,
        )
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

    def __next_navigation(self, soup):
        try:
            next_navigation = self.baseUrl + soup.select(self.selector)[0]["href"]
        except:
            return
        self.url_list.append(next_navigation)

    def getPageList(self) -> list:
        for i in self.url_list:
            soup = self.__soup(i)
            self.__next_navigation(soup)
        return self.url_list


class Parser(CrawlSite):
    def __init__(self, url, selector):
        super().__init__(url, selector)

    async def get_page(self, session, url):
        async with session.get(url) as r:
            return await r.text()

    async def get_all(self, session, urls):
        tasks = []
        for url in urls:
            task = asyncio.create_task(self.get_page(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

    async def main(self):
        self.getPageList()
        async with aiohttp.ClientSession() as session:
            data = await self.get_all(session, self.url_list)
            return data

    def parse(self, results):
        data = []
        for html in results:
            soup = BeautifulSoup(html, "html.parser")

            ## Multiple Item
            list_item = list((item["href"] for item in soup.select("a.g1-frame")))
            data.extend(list_item)
        return data
