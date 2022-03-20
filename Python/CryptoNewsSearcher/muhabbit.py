import requests
import asyncio
from bs4 import BeautifulSoup
import httpx


def links():
    url = "https://muhabbit.com/kategori/altcoin/"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    link = [i.select("a")[0]['href']
            for i in soup.select("li.mvp-blog-story-wrap")]
    return link


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
                          "h2" else i.text for i in soup.select(
                              "div#mvp-content-main")[0].select("p,h2")])
        result["M"+str(count)] = {'link': urls[count-1], 'text': text}
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
