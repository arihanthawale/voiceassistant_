from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Music:
    def __init__(self):
        chrome_service = Service(r'C:\webdrivers\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service=chrome_service)

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        time.sleep(2)  # Wait for the page to load

        # Find the first video in the search results
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
        video.click()
        time.sleep(100)  # Keep the browser open to watch the video

