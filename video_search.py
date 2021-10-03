from selenium import webdriver
from getVideoUrl import getVideoUrl
from bs4 import BeautifulSoup
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def video_search(query, count=5):
    options = webdriver.ChromeOptions()
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    options.headless = True
    main_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

    main_driver.get(getVideoUrl(query))
    sleep(0.2)
    soup = BeautifulSoup(main_driver.page_source, "lxml")
    videos = soup.find_all("a", id="thumbnail")

    res = []
    for i in range(0, min(count, len(videos))):
        try:
            res.append("https://www.youtube.com" + videos[i]["href"])
        except:
            pass

    main_driver.quit()

    return res
