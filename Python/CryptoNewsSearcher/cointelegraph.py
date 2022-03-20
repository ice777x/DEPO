import requests
from bs4 import BeautifulSoup
import asyncio
import httpx

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}


def links():
    r = requests.get("https://cointelegraph.com/tags/altcoin", headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    urls = ["https://cointelegraph.com"+i.select("a")[0]['href']
            for i in soup.select("article.post-card-inline")]
    return urls


async def main():
    urls = links()
    async with httpx.AsyncClient() as client:
        tasks = (client.get(url, headers=headers) for url in urls)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.content for req in reqs]
    count = 1
    result = {}
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        text = "\n".join(["\n"+i.text if i.name ==
                          "h2" else i.text for i in soup.select("div.post-content")[0].select("p,h2")])
        result["CTG"+str(count)] = {'link': urls[count-1], 'text': 'text'}
        count += 1
    return result


def search(word: str):
    founds = []
    try:
        for i in asyncio.run(main()).values():
            if word.upper() in i['text'].upper():
                founds.append(i)
    except:
        pass
    return founds
