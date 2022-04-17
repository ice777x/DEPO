import httpx
from time import time
import asyncio

kimlik = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"
}
linkler = (
    "https://www.trendyol.com/canavice/6-li-mutfak-havlusu-lavanta-seti-40x60-p-171630661",
    "https://www.trendyol.com/zeynep-tekstil/damask-4-lu-50x90-cm-el-yuz-havlu-seti-p-87609700",
    "https://www.trendyol.com/burtay-home/pamuklu-lux-boncuklu-gupurlu-havlu-6-li-50x90-rose-p-237085027",
    "https://www.trendyol.com/louis-marie/banyo-havlu-takimi-70x140-50x90-vip-kahve-p-52290033",
    "https://www.trendyol.com/minteks/kanavice-50x90-diva-6-li-havlu-takimi-krem-renk-p-59324344",
    "https://www.trendyol.com/kardelen/100-pamuklu-boncuklu-gupurlu-6-li-havlu-50x90-p-91250754",
    "https://www.trendyol.com/canavice/6-li-mutfak-havlusu-lavanta-seti-40x60-p-171630661",
    "https://www.trendyol.com/zeynep-tekstil/damask-4-lu-50x90-cm-el-yuz-havlu-seti-p-87609700",
    "https://www.trendyol.com/burtay-home/pamuklu-lux-boncuklu-gupurlu-havlu-6-li-50x90-rose-p-237085027",
    "https://www.trendyol.com/louis-marie/banyo-havlu-takimi-70x140-50x90-vip-kahve-p-52290033",
    "https://www.trendyol.com/minteks/kanavice-50x90-diva-6-li-havlu-takimi-krem-renk-p-59324344",
    "https://www.trendyol.com/kardelen/100-pamuklu-boncuklu-gupurlu-6-li-havlu-50x90-p-91250754",
    "https://www.trendyol.com/canavice/6-li-mutfak-havlusu-lavanta-seti-40x60-p-171630661",
    "https://www.trendyol.com/zeynep-tekstil/damask-4-lu-50x90-cm-el-yuz-havlu-seti-p-87609700",
    "https://www.trendyol.com/burtay-home/pamuklu-lux-boncuklu-gupurlu-havlu-6-li-50x90-rose-p-237085027",
    "https://www.trendyol.com/louis-marie/banyo-havlu-takimi-70x140-50x90-vip-kahve-p-52290033",
    "https://www.trendyol.com/minteks/kanavice-50x90-diva-6-li-havlu-takimi-krem-renk-p-59324344",
    "https://www.trendyol.com/kardelen/100-pamuklu-boncuklu-gupurlu-6-li-havlu-50x90-p-91250754",
    "https://www.trendyol.com/canavice/6-li-mutfak-havlusu-lavanta-seti-40x60-p-171630661",
    "https://www.trendyol.com/zeynep-tekstil/damask-4-lu-50x90-cm-el-yuz-havlu-seti-p-87609700",
    "https://www.trendyol.com/burtay-home/pamuklu-lux-boncuklu-gupurlu-havlu-6-li-50x90-rose-p-237085027",
    "https://www.trendyol.com/louis-marie/banyo-havlu-takimi-70x140-50x90-vip-kahve-p-52290033",
    "https://www.trendyol.com/minteks/kanavice-50x90-diva-6-li-havlu-takimi-krem-renk-p-59324344",
    "https://www.trendyol.com/kardelen/100-pamuklu-boncuklu-gupurlu-6-li-havlu-50x90-p-91250754",
    "https://www.trendyol.com/canavice/6-li-mutfak-havlusu-lavanta-seti-40x60-p-171630661",
    "https://www.trendyol.com/zeynep-tekstil/damask-4-lu-50x90-cm-el-yuz-havlu-seti-p-87609700",
    "https://www.trendyol.com/burtay-home/pamuklu-lux-boncuklu-gupurlu-havlu-6-li-50x90-rose-p-237085027",
    "https://www.trendyol.com/louis-marie/banyo-havlu-takimi-70x140-50x90-vip-kahve-p-52290033",
    "https://www.trendyol.com/minteks/kanavice-50x90-diva-6-li-havlu-takimi-krem-renk-p-59324344",
    "https://www.trendyol.com/kardelen/100-pamuklu-boncuklu-gupurlu-6-li-havlu-50x90-p-91250754"
)

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
