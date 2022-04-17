import httpx
from time import time
import asyncio

kimlik = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"
}
linkler = ["https://www.trendyol.com/sr?q=ceket&qt=ceket&st=ceket&os=1"]


def timer(func):  # decorator timer
    def wrapper():
        basla = time()
        func()
        print(f"\n{len(linkler)} Link : {time() - basla:.4f} saniye\n")

    return wrapper()


async def main():
    async with httpx.AsyncClient(headers=kimlik) as client:
        task = (client.get(url) for url in linkler)
        req = await asyncio.gather(*task)

    htmls = (re.text for re in req)

    for html in htmls:
        data = html.split("p-card-wrppr")
        print(len(data))

@timer
def parse():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
