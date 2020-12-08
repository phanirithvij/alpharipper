import urllib.parse as urlparse
from urllib.parse import parse_qs
from urllib.parse import urlencode, urlunparse

import requests
from bs4 import BeautifulSoup as soup
from requests.models import PreparedRequest

SELECTORS = {
    "wall":             "thumb-container-big",
    "mobile":           "item-element",
    "mobile:alt":       "thumb-element",
    "art":              "item",
    "pics":             "item",
    "avatars":          "avatar-thumb",
    "gifs":             "thumb-container",
    "covers":           "item",
    "covers:alt":       "thumb-container",
}


def get_pages(url: str) -> list:
    """
    The list of urls of the pages
    """
    if "page" not in url:
        pno = 0
        while True:
            pno += 1
            pgs = get_imgs_pgno(url, pno)
            if not pgs:
                # if not pgs or pno > 1:
                print(url, "done")
                break
            print("Found", len(pgs), get_subdomain(url), "items")
    else:
        # https://stackoverflow.com/a/7734686/8608146
        parsed = urlparse.urlparse(url)
        pq = parse_qs(parsed.query, keep_blank_values=True)
        # remove page from url
        page = pq.pop('page', None)[0]
        u = parsed._replace(query=urlencode(pq, True))
        url2 = urlunparse(u)
        pgs = get_imgs_pgno(url2, page)
        if not pgs:
            print("Invalid url", url)
            return
        print("found", len(pgs), get_subdomain(url), "items")
        print(url, "done")


# https://stackoverflow.com/a/49957974/8608146
def add_params(url, params):
    req = PreparedRequest()
    req.prepare_url(url, params)
    url = req.url
    return url


def singular_post(url):
    r = requests.get(url)
    souped = soup(r.content, "lxml")
    pic = souped.find("picture")
    # print(souped.select('a > picture > img'))
    if pic is not None and pic.parent.name == "a":
        print(pic.parent['href'])
        return pic.parent['href']
    print("not found", url)


def get_subdomain(url):
    return url.split('/')[2].split('.')[0]


def get_imgs_pgno(url, pageno, retry=None, param_retry=None):
    subdomain = get_subdomain(url)
    params = {'page': pageno}
    url_orig = url
    url = add_params(url, params)
    # print(url)
    try:
        r = requests.get(url)
    except Exception as e:
        print("Failed, retrying...")
        if retry is None:
            retry = 0
        if retry > 3:
            print(e)
            return
        return get_imgs_pgno(url_orig, pageno, retry=retry+1)
    parsed = urlparse.urlparse(r.url)
    p_params = parse_qs(parsed.query)
    # print(p_params, retry, param_retry)
    if 'page' not in p_params:
        # eg, name param was not given by user so server corrected it
        if param_retry is None:
            param_retry = 0
        if param_retry > 0:
            # page is being removed by the server so no next page
            print("No more pages")
            return
        url = r.url
        return get_imgs_pgno(url, pageno, param_retry=param_retry+1)
    elif p_params['page'][0] != str(pageno):
        # params is of the form {'page': ['1']}
        return
    urls = []
    souped = soup(r.content, "lxml")
    # for mobile, search, by-device, by-resolution have differnt selector
    if subdomain == "mobile":
        if not souped.find("div", {"class": SELECTORS[subdomain]}):
            subdomain = "mobile:alt"
    if subdomain == "covers":
        if not souped.find("div", {"class": SELECTORS[subdomain]}):
            subdomain = "covers:alt"
    # print(r.status_code, url,
    #     r.url, subdomain, SELECTORS[subdomain])
    for image in souped.find_all("div", {"class": SELECTORS[subdomain]}):
        t_url: str = image.find('img')['src']
        if subdomain == "gifs":
            t_url = image.find_all('img')[-1]['src']
        # remove thumb at the end
        x = t_url.split("/")
        dom = ("/".join(x[:-1]))
        # add the original url
        dom += f"/{x[-1].split('-')[-1]}"
        urls.append(dom)
    return urls
