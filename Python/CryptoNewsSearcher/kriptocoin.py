import httpx
from bs4 import BeautifulSoup
import requests
import asyncio

r = requests.get("https://kriptokoin.com/haberler/")

soup = BeautifulSoup(r.content, 'html.parser')

links = [i.select("h5.entry-title a")[0]['href']
         for i in soup.select("div.row article")]


async def main():

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in links)
        reqs = await asyncio.gather(*tasks)

    htmls = [req.content for req in reqs]
    result = {}
    count = 1
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        text = "\n".join(
            ["\n"+i.text if i.name ==
             "h3" else i.text for i in soup.select("div.post-content p, h3")])
        result["KK"+str(count)] = {"link": links[count-1], 'text': text}
        count += 1
    return result


def search(word: str):
    founds = []
    for i in asyncio.run(main()).values():
        if word.upper() in i['text'].upper():
            founds.append(i)
    return founds
