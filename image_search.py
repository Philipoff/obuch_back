from selenium import webdriver
from getImgUrl import getImgUrl
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
options.headless = True
main_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
additional_driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


def image_search(query, count=5):
    main_driver.get(getImgUrl(query))
    elems = main_driver.find_elements_by_xpath('//a[contains(@class, "wXeWr islib nfEiy")]')
    for i in range(0, count):
        elems[i].click()
        additional_driver.get(elems[i].get_attribute('href'))
        print(additional_driver.find_element_by_xpath('//img[contains(@class, "n3VNCb")]').get_attribute("src"))
    return 1

image_search("Котики")
main_driver.quit()
additional_driver.quit()