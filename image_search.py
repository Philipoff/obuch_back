import requests
from request_word import get_url
from bs4 import BeautifulSoup
from getImgUrl import getImgUrl

def image_search(query, count=5):
    response = requests.get(getImgUrl(query))
    soup = BeautifulSoup(response.text, 'lxml')

    quotes = soup.find_all('img')

    for i in range(1, count + 1):
        print(quotes[i]['src'])

image_search("Закат")