from bs4 import BeautifulSoup
import httpx
import asyncio


class GoogleSearch:
    def __init__(self, query: str):
        query = "%20".join(query.strip().split()) if query.split(" ") else query
        self.url = "https://www.google.com/search?q=" + query
        self.url_list = [self.url]
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
        self.data = []
        self.requests = httpx.Client(headers=self.headers)

    def __get_soup(self, url):
        r = self.requests.get(
            url,
            headers=self.headers,
        )
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

    def __next_navigation(self, soup, selector="#pnnext"):
        try:
            next_navigation = (
                "https://www.google.com" + soup.select(selector)[0]["href"]
            )
        except:
            return
        self.url_list.append(next_navigation)

    def __getSearchList(self) -> list:
        for i in self.url_list:
            soup = self.__get_soup(i)
            self.__next_navigation(soup)
        return self.url_list

    async def __main(self):
        site_list = self.__getSearchList()

        async with httpx.AsyncClient() as client:
            tasks = (client.get(url, headers=self.headers) for url in site_list)
            re = await asyncio.gather(*tasks)

        htmls = [req.content for req in re]
        for html in htmls:
            soup = BeautifulSoup(html, "html.parser")
            list_sites = (site["href"] for site in soup.select("div.yuRUbf a"))
            self.data.extend(list(list_sites))
        return

    def crawl(self):
        asyncio.run(self.__main())
        return self.data
