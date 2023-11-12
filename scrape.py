from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import requests

class Scrape:
    @staticmethod
    def runScrape():
        # Replace 'path/to/chromedriver' with the path to your chromedriver executable
        driver = webdriver.Chrome()

        # Open a website
        driver.get('https://wisc-housingdining.nutrislice.com/menu/gordon-avenue-market/breakfast/2023-11-11')
        driver.implicitly_wait(1000)
        # Get the title of the webpage
        title = driver.title
        print(f'Title of the webpage: {title}')
        # Close the browser
        element = driver.find_element(By.CSS_SELECTOR, '[data-testid="018026bcdb3445168421175d9ae4dd06"]')
        element.click()
        driver.implicitly_wait(10)
        element = driver.find_element(By.CLASS_NAME, 'content-container')
        element.click()
        elementSource = driver.find_element(By.ID, 'content').get_attribute("outerHTML")
        print(elementSource)
        print(elementSource.find("Avocado"))
        #r = requests.get()
        time.sleep(100)
