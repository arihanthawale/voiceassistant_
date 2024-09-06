from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class infow():
    def __init__(self):
        chrome_service = Service(r'C:\webdrivers\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def get_info(self, query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element(By.XPATH, '//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        enter.click()
        # Adding a delay to keep the browser open
        time.sleep(100)


