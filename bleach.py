import asyncio
import os
from pathlib import Path

from down import fetch_or_resume
from ripper import get_pages, get_subdomain


# https://stackoverflow.com/a/59385935/8608146
def background(f):
    def wrapped(*args, **kwargs):
        return asyncio.get_event_loop().run_in_executor(None, f, *args, **kwargs)

    return wrapped


@background
def dl_job(i, url):
    with open(f"progress/progress-{i}", 'a+') as progW:
        with open(f"progress/progress-{i}-failed", 'a+') as progF:
            data = []
            with open(f"progress/progress-{i}", 'r') as progR:
                data = progR.readlines()
                data = [l.strip() for l in data]
            if url not in data:
                dird = Path("downloads/"+get_subdomain(url))
                os.makedirs(dird, exist_ok=True)
                for x in get_pages(url):
                    for im in x:
                        fname = im.split('/')[-1]
                        fname = str(dird / fname)
                        if fname not in data:
                            try:
                                fetch_or_resume(im, fname, progress=False)
                                progW.write(fname + '\n')
                                progW.flush()
                            except Exception as e:
                                print("Failed to download", im, fname)
                                print(e)
                                progF.write(im + '\n')
                                progF.flush()
                        else:
                            print("Exists", im, fname)
                progW.write(url + '\n')
            else:
                print("Url done", url)


urls = [
    "https://wall.alphacoders.com/by_sub_category.php?id=174899&name=Bleach+Wallpapers",
    "https://mobile.alphacoders.com/by-sub-category/174899",
    "https://art.alphacoders.com/by_sub_category/174899",
    "https://pics.alphacoders.com/by_sub_category/174899",
    "https://avatars.alphacoders.com/by_sub_category/174899",
    "https://gifs.alphacoders.com/by_sub_category/174899",
    "https://covers.alphacoders.com/by_sub_category/174899"
]


async def main():
    listx = [dl_job(i, url) for i, url in enumerate(urls)]
    await asyncio.gather(*listx)

try:
    asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
    print("Abrupt shutdown")
    os.exit(-1)
