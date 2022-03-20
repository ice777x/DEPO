import urllib.request
from urllib.error import ContentTooShortError
import requests
from bs4 import BeautifulSoup
import os


def books(query: str):
    if not os.path.exists("Books"):
        os.makedirs("Books")
    session = requests.Session()
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/91.0.4472.124 Safari/537.36"
        )
    })
    r = requests.get(
        f"http://libgen.is/search.php?&res=100&req={query}&phrase=1&view=simple&column=def&sort=year&sortmode=DESC"
    )
    soup = BeautifulSoup(r.content, "html.parser")

    book_urls = soup.find_all("a", {"title": "this mirror"})
    r = soup.select("table.c")[0].select("tr td:nth-child(3)")[1:]
    books = [
        {"book_name": v.find("a").text, "book_url": book_urls[i]["href"]}
        for i, v in enumerate(r)
    ]
    for z in books:
        re = requests.get(z["book_url"])
        soup2 = BeautifulSoup(re.content, "html.parser")
        book_down_link = (
            soup2.select("div#download")[0].select("ul")[0].find("a")["href"]
        )
        book_real_name = z["book_name"].strip().replace(
            " ", "_") + "." + book_down_link[::-1].split(".", 1)[0][::-1]
        try:
            urllib.request.urlretrieve(
                book_down_link, "Books/" + book_real_name)
        except ContentTooShortError:
            urllib.request.urlretrieve(
                book_down_link, "Books/" + book_real_name)


books()
