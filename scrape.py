from selenium import webdriver
import time

from selenium.webdriver.common.by import By


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
        time.sleep(100)