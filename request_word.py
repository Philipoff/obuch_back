# -*- coding: utf-8 -*-

from googlesearch import search


def get_url(search_word):
    urls = []
    for url in search(search_word, tld='ru', lang='ru', stop=8):
        if "http" in url and ".pdf" not in url:
            urls.append(url)
    return urls
