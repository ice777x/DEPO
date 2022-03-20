import asyncio
import httpx
import requests
from bs4 import BeautifulSoup


def links():
    url = "https://beincrypto.com.tr/haberler/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return [i.select("a")[0]['href'] for i in soup.select("article")]


async def main():
    urls = links()
    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        reqs = await asyncio.gather(*tasks)
    htmls = [req.content for req in reqs]
    result = {}
    count = 1
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        text = "\n".join(["\n"+i.text if i.name ==
                          "h3" else i.text for i in soup.select(
                              "div.entry-content-inner")[0].select("p,h3")[:-1]])
        result["BC"+str(count)] = {'link': urls[count-1], 'text': text}
        count += 1
    return result


def search(word: str):
    founds = []
    for i in asyncio.run(main()).values():
        if word.upper() in i['text'].upper():
            founds.append(i)
    return founds
