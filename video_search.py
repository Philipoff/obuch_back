from selenium import webdriver
from getVideoUrl import getVideoUrl
from bs4 import BeautifulSoup
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
options.headless = True
main_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

def video_search(query, count=5):
    main_driver.get(getVideoUrl(query))
    sleep(0.2)
    soup = BeautifulSoup(main_driver.page_source, "lxml")
    videos = soup.find_all("a", id="thumbnail")
    for i in range(0, count):
        print("https://www.youtube.com" + videos[i]["href"])
    return

video_search("")

main_driver.quit()