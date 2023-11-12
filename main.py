from gui import GUI
from scrape import Scrape

if __name__ == '__main__':
    #GUI.runGUI()
    Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/gordon-avenue-market/breakfast/2023-11-11')
    Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/four-lakes-market/breakfast/2023-11-11')
    Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/carsons-market/lunch/2023-11-11')
    Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/lizs-market/breakfast/2023-11-11')
    Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/rhetas-market/breakfast/2023-11-11')
