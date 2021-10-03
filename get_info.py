import requests
from bs4 import BeautifulSoup


def get_info(site):
    site_type = "all"
    if ".jpg" in site or ".png" in site:
        site_type = "image"
    if "www.youtube.com" in site:
        site_type = "video"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/92.0.4515.159 YaBrowser/21.8.3.614 Yowser/2.5 Safari/537.36',
    }
    resp = requests.get(site, headers=headers)
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, features="html.parser")

    title = soup.find("title")
    metas = soup.find_all('meta')

    description = [meta.attrs['content'] for meta in metas if
                   'name' in meta.attrs and meta.attrs['name'].lower() == 'description']
    icon_link = soup.find("link", rel="shortcut icon")

    info = {
        "link": site,
        "title": title.text.strip() if title else '',
        "icon": icon_link.attrs["href"] if icon_link else '',
        "description": description[0].strip() if len(description) > 0 else '',
        "type": site_type
    }
    return info
