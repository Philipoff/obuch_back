from googlesearch import search


def get_url(search_word):
    urls = []
    for url in search(search_word, tld='ru', lang='ru', stop=5):
        urls.append(url)
    return urls
