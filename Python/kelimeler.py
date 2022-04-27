from bs4 import BeautifulSoup
import aiohttp
import asyncio


class KelimeListesi:
    """
    c = KelimeListesi()

    c.parse("z")
    """

    letter: str

    def __init__(self):
        self.letter = ""

    async def get_requests(self, session, url):
        async with session.get(url) as r:
            return await r.text()

    async def get_all(self, session):
        url_list = []
        for i in range(3, 16):
            try:
                url_list.append(
                    f"https://kelimeler.net/{self.letter.upper()}-ile-baslayan-{i}-harfli-kelimeler"
                )
            except:
                continue
        tasks = (
            asyncio.ensure_future(self.get_requests(session, url)) for url in url_list
        )
        result = await asyncio.gather(*tasks)
        return result

    async def main(self) -> list:
        async with aiohttp.ClientSession() as session:
            data = await self.get_all(session)
            return data

    def parse(self, letter: str):
        self.letter = letter
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        results = asyncio.run(self.main())
        data = []
        for html in results:
            soup = BeautifulSoup(html, "html.parser")
            data.extend(
                list(
                    (
                        kelime.text.strip().replace("İ", "I")
                        for kelime in soup.select("a.ListedWordLink")
                    )
                )
            )
        return data
