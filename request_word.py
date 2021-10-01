from googlesearch import search


def get_url(search_word):
    for url in search(search_word, tld='ru', lang='ru', stop=20):
        print(url)
