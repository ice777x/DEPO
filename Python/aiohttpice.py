import asyncio
import aiohttp
from time import time

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
)


def timer(func):  # decorator timer
    def wrapper():
        basla = time()
        func()
        print(f"\n{len(linkler)} Link : {time() - basla:.4f} saniye\n")

    return wrapper()


async def get_page(session, url):
    async with session.get(url) as r:
        return await r.text()


async def get_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(get_page(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def main():
    async with aiohttp.ClientSession(headers=kimlik) as session:
        data = await get_all(session, linkler)
        return data


@timer
def parse():
    data = []
    results = asyncio.run(main())
    for html in results:
        data = html.split("<title>")[1].split("</title>")[0]
        print(data)
    return
