import selenium.common.exceptions
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
import requests
from Item import Item

class Scrape:
    @staticmethod
    def runScrape(url):
        calories = []
        breakfast = []
        lunch = []
        dinner = []

        def countCalories():
            calorieIndex = elementSource.find("Calories")
            if calorieIndex == -1:
                return 0
            calories = ""
            startIndex = 0
            for x in range(calorieIndex, calorieIndex + 50):
                if elementSource[x] == '>':
                    startIndex = x
                    break

            for x in range(startIndex + 1, startIndex + 1 + elementSource[startIndex + 1:startIndex + 6].find('<')):
                calories += elementSource[x]
            if calories == '':
                return 0
            calories = int(calories)
            return calories

        def countProtein():
            protein = ""
            startIndex = 0
            proteinIndex = elementSource.find("Protein:")
            if proteinIndex == -1:
                return 0
            for x in range(proteinIndex + 16, proteinIndex + 100):
                if elementSource[x] == '>':
                    startIndex = x
                    break

            for x in range(startIndex + 1, startIndex + 1 + elementSource[startIndex + 1:startIndex + 6].find('<')):
                protein += elementSource[x]

            protein = int(protein[:-2])
            return protein

        def getName():
            name = ""

            hi = driver.find_element(By.CLASS_NAME, 'name').get_attribute("outerHTML")
            for x in range(hi.find(">") + 2, hi.find("<!") - 1):
                name += hi[x]
                print(x)

            return name

        # Replace 'path/to/chromedriver' with the path to your chromedriver executable
        driver = webdriver.Chrome()

        # Open a website
        driver.get(url)
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
        driver.implicitly_wait(10)
        elementSource = driver.find_element(By.CLASS_NAME, 'info-container').get_attribute("outerHTML")
        print(elementSource)

        for i in range(500):
            try:
                elementSource = driver.find_element(By.CLASS_NAME, 'info-container').get_attribute("outerHTML")

                if countCalories() not in calories:
                    calories.append(countCalories())
                    item = Item()
                    item.setProtein(countProtein())
                    item.setCalories(countCalories())
                    item.setName(getName())
                    goThroughLoop = True
                    try:
                        element = driver.find_element(By.CLASS_NAME, 'icons-list')
                        testArray = element.text.split("\n")
                    except selenium.common.exceptions.NoSuchElementException:
                        goThroughLoop = False

                    vegan = False
                    vegetarian = False
                    halal = False
                    dairy = False
                    egg = False
                    wheat = False
                    sesame = False
                    corn = False
                    soy = False
                    coconut = False
                    nuts = False
                    milk = False
                    if goThroughLoop == True:
                        for pref in testArray:
                            if pref == "Vegan":
                                vegan = True
                            if pref == "Vegetarian":
                                vegetarian = True
                            if pref == "Halal":
                                halal = True
                            if pref == "Dairy":
                                dairy = True
                            if pref == "Egg":
                                egg = True
                            if pref == "Wheat":
                                wheat = True
                            if pref == "Sesame":
                                sesame = True
                            if pref == "Corn":
                                corn = True
                            if pref == "Soy":
                                soy = True
                            if pref == "Coconut":
                                coconut = True
                            if pref == "Nuts":
                                nuts = True
                            if pref == "Milk":
                                milk = True

                    item.setPreferences([vegan, vegetarian, halal])
                    item.setPreferences([dairy, egg, wheat, sesame, corn, soy, coconut, nuts, milk])

                    breakfast.append(item)
                    goThroughLoop = True
                element = driver.find_element(By.CLASS_NAME, 'ns-icon-right-arrow')
                element.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                break
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        calories.clear();
        for i in range(6):
            webdriver.ActionChains(driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
            webdriver.ActionChains(driver).key_up(Keys.SHIFT).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

        driver.implicitly_wait(10)
        element = driver.find_element(By.CLASS_NAME, 'content-container')
        element.click()

        for i in range(500):
            try:
                elementSource = driver.find_element(By.CLASS_NAME, 'info-container').get_attribute("outerHTML")
                if countCalories() not in calories:
                    calories.append(countCalories())
                    item = Item()
                    item.setProtein(countProtein())
                    item.setCalories(countCalories())
                    item.setName(getName())
                    goThroughLoop = True
                    try:
                        element = driver.find_element(By.CLASS_NAME, 'icons-list')
                        testArray = element.text.split("\n")
                    except selenium.common.exceptions.NoSuchElementException:
                        goThroughLoop = False

                    vegan = False
                    vegetarian = False
                    halal = False
                    dairy = False
                    egg = False
                    wheat = False
                    sesame = False
                    corn = False
                    soy = False
                    coconut = False
                    nuts = False
                    milk = False
                    if goThroughLoop == True:
                        for pref in testArray:
                            if pref == "Vegan":
                                vegan = True
                            if pref == "Vegetarian":
                                vegetarian = True
                            if pref == "Halal":
                                halal = True
                            if pref == "Dairy":
                                dairy = True
                            if pref == "Egg":
                                egg = True
                            if pref == "Wheat":
                                wheat = True
                            if pref == "Sesame":
                                sesame = True
                            if pref == "Corn":
                                corn = True
                            if pref == "Soy":
                                soy = True
                            if pref == "Coconut":
                                coconut = True
                            if pref == "Nuts":
                                nuts = True
                            if pref == "Milk":
                                milk = True

                    item.setPreferences([vegan, vegetarian, halal])
                    item.setPreferences([dairy, egg, wheat, sesame, corn, soy, coconut, nuts, milk])

                    lunch.append(item)

                element = driver.find_element(By.CLASS_NAME, 'ns-icon-right-arrow')
                element.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                break
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        calories.clear();
        for i in range(5):
            webdriver.ActionChains(driver).key_down(Keys.SHIFT).perform()
            webdriver.ActionChains(driver).send_keys(Keys.TAB).perform()
            webdriver.ActionChains(driver).key_up(Keys.SHIFT).perform()
        webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()

        driver.implicitly_wait(10)
        element = driver.find_element(By.CLASS_NAME, 'content-container')
        element.click()

        for i in range(500):
            try:
                elementSource = driver.find_element(By.CLASS_NAME, 'info-container').get_attribute("outerHTML")
                if countCalories() not in calories:
                    calories.append(countCalories())
                    item = Item()
                    item.setProtein(countProtein())
                    item.setCalories(countCalories())
                    item.setName(getName())
                    goThroughLoop = True
                    try:
                        element = driver.find_element(By.CLASS_NAME, 'icons-list')
                        testArray = element.text.split("\n")
                    except selenium.common.exceptions.NoSuchElementException:
                        goThroughLoop = False

                    vegan = False
                    vegetarian = False
                    halal = False
                    dairy = False
                    egg = False
                    wheat = False
                    sesame = False
                    corn = False
                    soy = False
                    coconut = False
                    nuts = False
                    milk = False
                    if goThroughLoop == True:
                        for pref in testArray:
                            if pref == "Vegan":
                                vegan = True
                            if pref == "Vegetarian":
                                vegetarian = True
                            if pref == "Halal":
                                halal = True
                            if pref == "Dairy":
                                dairy = True
                            if pref == "Egg":
                                egg = True
                            if pref == "Wheat":
                                wheat = True
                            if pref == "Sesame":
                                sesame = True
                            if pref == "Corn":
                                corn = True
                            if pref == "Soy":
                                soy = True
                            if pref == "Coconut":
                                coconut = True
                            if pref == "Nuts":
                                nuts = True
                            if pref == "Milk":
                                milk = True

                    item.setPreferences([vegan, vegetarian, halal])
                    item.setPreferences([dairy, egg, wheat, sesame, corn, soy, coconut, nuts, milk])

                    dinner.append(item)

                element = driver.find_element(By.CLASS_NAME, 'ns-icon-right-arrow')
                element.click()
            except selenium.common.exceptions.ElementClickInterceptedException:
                break
        calories.clear()
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        print("breakfast")
        print(breakfast)
        print("lunch")
        print(lunch)
        print("dinner")
        print(dinner)
