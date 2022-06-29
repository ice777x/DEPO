import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import fastapi

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}


base = "https://wallpaperaccess.com"

data = []
def get_urls(query: str):
    r = requests.get("https://wallpaperaccess.com/search?q=" + query, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    urls = [base + i["href"] for i in soup.select("a.image")]
    return urls


async def get_page(session, url):
    async with session.get(url) as resp:
        return await resp.text("unicode_escape")


async def print_response(session, url):
    html = await get_page(session, url)
    soup = BeautifulSoup(html, "html.parser")
    imgs = soup.select("img.thumb")
    data.extend(
        [
            "https://wallpaperaccess.com" + i["data-src"] if not i.has_attr("src") else i["src"]
            for i in imgs
        ]
    )


async def main(q: str):
    urls = get_urls(q)
    async with aiohttp.ClientSession(headers=headers) as session:
        tasks = [asyncio.create_task(print_response(session, url)) for url in urls[:10]]
        await asyncio.gather(*tasks)
    return data
