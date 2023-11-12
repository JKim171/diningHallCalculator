import tkinter as tk
from tkinter import *
from tkinter import font
import ttkbootstrap as ttk

from Item import Item
from scrape import Scrape


class GUI:

    @staticmethod
    def runGUI():

        locationsKey = [ "Rheta", "Gordon", "Lowell", "Liz", "Carson", "Flakes" ]
        locations = [False, False, False, False, False, False]
        timeKey = [ "Breakfast", "Lunch", "Dinner" ]
        time = [False, False, False]
        preferencesKey = [ "Vegan", "Vegetarian", "Halal" ]
        preferences = [False, False, False]
        allergiesKey = [ "Dairy", "Egg", "Wheat", "Sesame", "Corn", "Soy", "Coconut", "Nuts", "Fish", "Milk" ]
        allergies = [False, False, False, False, False, False, False, False, False, False]
        selectedLocation = -1
        root = ttk.Window(title="Dining Hall Calculator", themename="darkly", size=(1920, 1080))
        allMarkets = []

        currentFrame = None

        def createItems(itemList, newWindow):
            #itemFrame.destroy()

            itemsFrame = tk.Frame(newWindow, padx=20, pady=0)
            itemsFrame.pack(side="top", anchor="nw")
            itemTopLevelFrame = tk.Frame(itemsFrame, padx=20, pady=0)
            itemTopLevelFrame.pack(side="top", anchor="nw")
            itemMiddleLevelFrame = tk.Frame(itemsFrame, padx=20, pady=0)
            itemMiddleLevelFrame.pack(side="top", anchor="nw")
            itemBottomLevelFrame = tk.Frame(itemsFrame, padx=20, pady=0)
            itemBottomLevelFrame.pack(side="top", anchor="nw")

            frame = itemsFrame



            allItemFrames = []
            for i in range(len(itemList)):
                item = itemList[i]
                if i < 9:
                    if i < 3:
                        allItemFrames.append(tk.Frame(itemTopLevelFrame, padx=20, pady=0))
                        allItemFrames[i].pack(side="left", anchor="nw")
                    elif i < 6:
                        allItemFrames.append(tk.Frame(itemMiddleLevelFrame, padx=20, pady=0))
                        allItemFrames[i].pack(side="left", anchor="nw")
                    else:
                        allItemFrames.append(tk.Frame(itemBottomLevelFrame, padx=20, pady=0))
                        allItemFrames[i].pack(side="left", anchor="nw")

                    nameLabel = ttk.Label(allItemFrames[i], text=item.getName(), bootstyle="solar",
                                          font=font.Font(family="Arial", size=30))
                    nameLabel.pack(side="top", anchor="nw")
                    calLabel = ttk.Label(allItemFrames[i], text=str(item.getCalories()) + " Calories",
                                         bootstyle="solar",
                                         font=font.Font(family="Arial", size=25))
                    calLabel.pack(side="top", anchor="nw")
                    proteinLabel = ttk.Label(allItemFrames[i], text=str(item.getProtein()) + "g Protein",
                                             bootstyle="solar",
                                             font=font.Font(family="Arial", size=25))
                    proteinLabel.pack(side="top", anchor="nw")
            return frame

        def activateNW(button, locations, newWindow):
            button.configure(bootstyle="info-toolbutton", command=lambda: deactivateNW(button, locations))
            bText = button.cget("text")
            for i in range(len(locations)):
                if bText == locations[i].cget("text"):
                    selectedLocation = i
                    createItems(allMarkets[selectedLocation], newWindow)
                    #setItems(selectedLocation)
                    for a in range(len(locations)):
                        if a!=i:
                            deactivateNW(locations[a], locations)
        def deactivateNW(button, locations):
            button.configure(bootstyle="info-outline", command=lambda: activateNW(button, locations,newWindow))
            bText = button.cget("text")

        def setItems(selectedLocation):
            global currentFrame
            itemsFrame = tk.Frame(newWindow, padx=20, pady=0)
            itemsFrame.pack(side="top", anchor="nw")
            if currentFrame == None:
                currentFrame = createItems(allMarkets[selectedLocation], newWindow, itemsFrame)
            else:
                currentFrame = createItems(allMarkets[selectedLocation], newWindow, currentFrame)
        def activate(button):
            button.configure(bootstyle="info-toolbutton", command=lambda: deactivate(button))
            # getting button values
            bText = button.cget("text")
            if bText == "Rheta's Market":
                locations[0] = True
            if bText == "Gordon Avenue Market":
                locations[1] = True
            if bText == "Lowell Market":
                locations[2] = True
            if bText == "Liz's Market":
                locations[3] = True
            if bText == "Carson's Market":
                locations[4] = True
            if bText == "Four Lakes Market":
                locations[5] = True
            if bText == "Breakfast":
                time[0] = True
                deactivate(lunchButton)
                deactivate(dinnerButton)
            if bText == "Lunch":
                time[1] = True
                deactivate(breakfastButton)
                deactivate(dinnerButton)
            if bText == "Dinner":
                time[2] = True
                deactivate(lunchButton)
                deactivate(breakfastButton)

        def deactivate(button):
            button.configure(bootstyle="info-outline", command=lambda: activate(button))
            bText = button.cget("text")
            if bText == "Rheta's Market":
                locations[0] = False
            if bText == "Gordon Avenue Market":
                locations[1] = False
            if bText == "Lowell Market":
                locations[2] = False
            if bText == "Liz's Market":
                locations[3] = False
            if bText == "Carson's Market":
                locations[4] = False
            if bText == "Four Lakes Market":
                locations[5] = False
            if bText == "Breakfast":
                time[0] = False
            if bText == "Lunch":
                time[1] = False
            if bText == "Dinner":
                time[2] = False

        def submit(minCaloriesEntry, maxCaloriesEntry, minProteinEntry, maxProteinEntry):
            global newWindow
            itemList = []   
            def comparePref(item, prefArray):
                for i in range(len(item.getPreferences())):
                    if (item.getPreferences()[i] == True) and (prefArray[i] != True):
                        return False
                return True

            def compareAllergies(item, allergiesArray):
                for i in range(len(item.getPreferences())):
                    if (item.getAllergies()[i] == True) and (allergiesArray[i] == True):
                        return False
                return True

            def compareCalories(item):
                if item.getCalories() > minCalories and item.getCalories < maxCalories:
                    return True
                else:
                    return False

            def compareProtein(item):
                if item.getProtein() > minProtein and item.getProtein < maxProtein:
                    return True
                else:
                    return False

            try:
                minCalories = int(minCaloriesEntry.get())
                maxCalories = int(maxCaloriesEntry.get())
                minProtein = int(minProteinEntry.get())
                maxProtein = int(maxProteinEntry.get())
            except ValueError:
                print("Please input a valid integer")
                minCalories = 0
                maxCalories = 0
                minProtein = 0
                maxProtein = 0
            calories = [minCalories, maxCalories]
            protein = [minProtein, maxProtein]
            preferences = [veganInt.get() == 1, vegetarianInt.get() == 1, halalInt.get() == 1]

            # [ Dairy, Egg, Wheat, Sesame, Corn, Soy, Coconut, Nuts, Milk ]
            allergies = [dairyInt.get() == 1, eggInt.get() == 1, wheatInt.get() == 1, sesameInt.get() == 1,
                         cornInt.get() == 1, soyInt.get() == 1, coconutInt.get() == 1, nutsInt.get() == 1,
                         milkInt.get() == 1]
            allRestrictions = [locations, time, calories, protein, preferences, allergies]
            rhetasScrape = None
            gordonScrape = None
            lowellScrape = None
            lizScrape = None
            carsonScrape = None
            flakesScrape = None
            if locations[0] == True:
                rhetasScrape = Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/rhetas-market/lunch/')
                rhetasScrape = rhetasScrape[1:]
                for i, n in enumerate(time):
                    if n:
                        rhetasScrape = rhetasScrape[i]
                for i, n in enumerate(rhetasScrape):
                    if (comparePref(rhetasScrape[i], preferences)):
                        if (compareAllergies(rhetasScrape[i], allergies)):
                            if (n.getCalories() >= calories[0] and n.getCalories() <= calories[1]):
                                if (n.getProtein() >= protein[0] and n.getProtein() <= protein[1]):
                                    itemList.append(n)
                allMarkets.append(itemList)
            if locations[1] == True:
                gordonScrape = Scrape.runScrape(
                    'https://wisc-housingdining.nutrislice.com/menu/gordon-avenue-market/breakfast/')
                for i, n in enumerate(time):
                    if n:
                        gordonScrape = gordonScrape[i]
                for i, n in enumerate(gordonScrape):
                    if (comparePref(gordonScrape[i], preferences)):
                        if (compareAllergies(gordonScrape[i], allergies)):
                            if (n.getCalories() >= calories[0] and n.getCalories() <= calories[1]):
                                if (n.getProtein() >= protein[0] and n.getProtein() <= protein[1]):
                                    itemList.append(n)
                allMarkets.append(itemList)
            if locations[2] == True:
                lowellScrape = None
            if locations[3] == True:
                lizScrape = None
            if locations[4] == True:
                carsonScrape = Scrape.runScrape('https://wisc-housingdining.nutrislice.com/menu/carsons-market/lunch/')
                carsonScrape = carsonScrape[1:]
                for i, n in enumerate(time):
                    if n:
                        carsonScrape = carsonScrape[i]
                for i, n in enumerate(carsonScrape):
                    if (comparePref(carsonScrape[i], preferences)):
                        if (compareAllergies(carsonScrape[i], allergies)):
                            if (n.getCalories() >= calories[0] and n.getCalories() <= calories[1]):
                                if (n.getProtein() >= protein[0] and n.getProtein() <= protein[1]):
                                    itemList.append(n)
                allMarkets.append(itemList)
            if locations[5] == True:
                flakesScrape = Scrape.runScrape(
                    'https://wisc-housingdining.nutrislice.com/menu/four-lakes-market/breakfast/')
                for i, n in enumerate(time):
                    if n:
                        flakesScrape = flakesScrape[i]
                for i, n in enumerate(flakesScrape):
                    if (comparePref(flakesScrape[i], preferences)):
                        if (compareAllergies(flakesScrape[i], allergies)):
                            if (n.getCalories() >= calories[0] and n.getCalories() <= calories[1]):
                                if (n.getProtein() >= protein[0] and n.getProtein() <= protein[1]):
                                    itemList.append(n)
                allMarkets.append(itemList)
            print("this is the itemList below")
            print(allMarkets)


            newWindow = Toplevel(root)
            newWindow.geometry('3000x1000')

            topFrame = tk.Frame(newWindow, padx=20, pady=0)
            topFrame.pack(side="top", anchor="nw")

            middleFrame = tk.Frame(newWindow, padx=20, pady=0)
            middleFrame.pack(side="top", anchor="nw")

            bottomFrame = tk.Frame(newWindow, padx=20, pady=0)
            bottomFrame.pack(side="top", anchor="nw")

            titleLabel = tk.Label(topFrame, text="Your Preferences: ",
                                        font=font.Font(family="Arial", size=34))
            titleLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            timeString =""
            for i in range (len(time)):
                if time[i]:
                    timeString = timeKey[i]

            yourTimeLabel = tk.Label(topFrame, text=timeString,
                                            font=font.Font(family="Arial", size=34))
            yourTimeLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            preferencesString = ""
            for i in range (len(preferences)):
                if preferences[i]:
                    preferencesString += preferencesKey[i] + ", "
            preferencesString = preferencesString[:-2]

            yourPreferencesLabel = tk.Label(topFrame, text=preferencesString,
                                     font=font.Font(family="Arial", size=34))
            yourPreferencesLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            allergiesString = ""
            firstAdd = True
            for i in range (len(allergies)):
                if allergies[i]:
                    if firstAdd:
                        allergiesString += "NO "
                        firstAdd=False
                    allergiesString += allergiesKey[i] + ", "
            allergiesString = allergiesString[:-2]

            yourAllergiesLabel = tk.Label(middleFrame, text=allergiesString,
                                            font=font.Font(family="Arial", size=34))
            yourAllergiesLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            yourCaloriesLabel = tk.Label(bottomFrame, text=str(calories[0])+ " - " +str(calories[1]) + " Calories",
                                          font=font.Font(family="Arial", size=34))
            yourCaloriesLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            yourProteinLabel = tk.Label(bottomFrame, text=str(protein[0]) + "g - " +str(protein[1]) + "g Protein",
                                          font=font.Font(family="Arial", size=34))
            yourProteinLabel.pack(side="left", padx=40, anchor="nw", pady=20)

            hallsFrame = tk.Frame(newWindow, padx=20, pady=0)
            hallsFrame.pack(side="top", anchor="nw")

            rhetasButtonNew = ttk.Button(hallsFrame, text="Rheta's Market", bootstyle="info-outline",
                                         command=lambda: activateNW(rhetasButtonNew, locationButtons, newWindow))
            gordonButtonNew = ttk.Button(hallsFrame, text="Gordon Avenue Market",bootstyle="info-outline",
                                      command=lambda: activateNW(gordonButtonNew, locationButtons,newWindow))
            lowellButtonNew = ttk.Button(hallsFrame, text="Lowell Market",bootstyle="info-outline",
                                      command=lambda: activateNW(lowellButtonNew, locationButtons,newWindow))
            lizButtonNew = ttk.Button(hallsFrame, text="Liz's Market",bootstyle="info-outline",
                                   command=lambda: activateNW(lizButtonNew, locationButtons,newWindow))
            carsonButtonNew = ttk.Button(hallsFrame, text="Carson's Market",bootstyle="info-outline",
                                      command=lambda: activateNW(carsonButtonNew, locationButtons,newWindow))
            fourLakesButtonNew = ttk.Button(hallsFrame, text="Four Lakes Market",bootstyle="info-outline",
                                         command=lambda: activateNW(fourLakesButtonNew, locationButtons,newWindow))
            locationButtons = [rhetasButtonNew, gordonButtonNew, lowellButtonNew, lizButtonNew, carsonButtonNew, fourLakesButtonNew]

            #will change for most options
            for i in range(len(locations)):
                if locations[i]:
                    locationButtons[i].pack(side="left", padx=20)

            itemsFrame = tk.Frame(newWindow, padx=20, pady=0)
            itemsFrame.pack(side="top", anchor="nw")
            currentFrame  = itemsFrame














            #debug
            print(locations)
            print(time)
            print(preferences)
            print(allergies)
            print(protein)
            print(calories)


        diningHallFrame = tk.Frame(root, padx=20, pady=20)
        diningHallFrame.pack(side="top", anchor="nw")


        diningHallLabel = ttk.Label(diningHallFrame, text="Dining Hall:", bootstyle="solar",
                                    font=font.Font(family="Arial", size=34))
        diningHallLabel.pack(side="top", anchor="nw", padx=20)

        diningHallButtonFrame = tk.Frame(root, padx=20, pady=20)
        diningHallButtonFrame.pack(side="top", anchor="nw")

        rhetasButton = ttk.Button(diningHallButtonFrame, text="Rheta's Market", bootstyle="info-outline",
                                  command=lambda: activate(rhetasButton))
        rhetasButton.pack(side="left", padx=20)

        gordonButton = ttk.Button(diningHallButtonFrame, text="Gordon Avenue Market", bootstyle="info-outline",
                                  command=lambda: activate(gordonButton))
        gordonButton.pack(side="left", padx=20)

        lowellButton = ttk.Button(diningHallButtonFrame, text="Lowell Market", bootstyle="info-outline",
                                  command=lambda: activate(lowellButton))
        lowellButton.pack(side="left", padx=20)

        lizButton = ttk.Button(diningHallButtonFrame, text="Liz's Market", bootstyle="info-outline",
                               command=lambda: activate(lizButton))
        lizButton.pack(side="left", padx=20)

        carsonButton = ttk.Button(diningHallButtonFrame, text="Carson's Market", bootstyle="info-outline",
                                  command=lambda: activate(carsonButton))
        carsonButton.pack(side="left", padx=20)

        fourLakesButton = ttk.Button(diningHallButtonFrame, text="Four Lakes Market", bootstyle="info-outline",
                                     command=lambda: activate(fourLakesButton))
        fourLakesButton.pack(side="left", padx=20)


        timeLabelFrame = tk.Frame(root, padx=20, pady=20)
        timeLabelFrame.pack(side="top", anchor="nw")

        timeLabel = ttk.Label(timeLabelFrame, text="Time:", bootstyle="solar",
                              font=font.Font(family="Arial", size=34))
        timeLabel.pack(side="top", anchor="nw", padx=20)

        timeFrame = tk.Frame(root, padx=20, pady=20)
        timeFrame.pack(side="top", anchor="nw")

        breakfastButton = ttk.Button(timeFrame, text="Breakfast", bootstyle="info-outline",
                                     command=lambda: activate(breakfastButton))
        breakfastButton.pack(side="left", padx=20)

        lunchButton = ttk.Button(timeFrame, text="Lunch", bootstyle="info-outline",
                                 command=lambda: activate(lunchButton))
        lunchButton.pack(side="left", padx=20)

        dinnerButton = ttk.Button(timeFrame, text="Dinner", bootstyle="info-outline",
                                  command=lambda: activate(dinnerButton))
        dinnerButton.pack(side="left", padx=20)

        macrosFrame = tk.Frame(root, padx=20, pady=20)
        macrosFrame.pack(side="top", anchor="nw")

        macrosLabel = ttk.Label(macrosFrame, text="Macros:", bootstyle="solar",
                                font=font.Font(family="Arial", size=34))
        macrosLabel.pack(side="top", anchor="nw", padx=20)

        macrosSlidersFrame = tk.Frame(root, padx=20, pady=20)
        macrosSlidersFrame.pack(side="top", anchor="nw")

        minCaloriesLabel = ttk.Label(macrosSlidersFrame, text="Minimum Calories:", bootstyle="solar",
                                     font=font.Font(family="Arial", size=20))
        minCaloriesLabel.pack(side="left", padx=20)

        minCaloriesEntry = ttk.Entry(macrosSlidersFrame)
        minCaloriesEntry.pack(side="left", padx=20)

        maxCaloriesLabel = ttk.Label(macrosSlidersFrame, text="Maximum Calories:", bootstyle="solar",
                                     font=font.Font(family="Arial", size=20))
        maxCaloriesLabel.pack(side="left")

        maxCaloriesEntry = ttk.Entry(macrosSlidersFrame)
        maxCaloriesEntry.pack(side="left", padx=20)

        proteinFrame = tk.Frame(root, padx=20, pady=20)
        proteinFrame.pack(side="top", anchor="nw")

        minProteinLabel = ttk.Label(proteinFrame, text="Minimum Protein (grams):", bootstyle="solar",
                                    font=font.Font(family="Arial", size=20))
        minProteinLabel.pack(side="left", padx=20)

        minProteinEntry = ttk.Entry(proteinFrame)
        minProteinEntry.pack(side="left", padx=20)

        maxProteinLabel = ttk.Label(proteinFrame, text="Maximum Protein (grams):", bootstyle="solar",
                                    font=font.Font(family="Arial", size=20))
        maxProteinLabel.pack(side="left")

        maxProteinEntry = ttk.Entry(proteinFrame)
        maxProteinEntry.pack(side="left", padx=20)

        preferencesLabel = ttk.Label(root, text="Preferences:", bootstyle="solar",
                                     font=font.Font(family="Arial", size=34))
        preferencesLabel.pack(side="top", anchor="nw", padx=40, pady=20)

        preferencesFrame = tk.Frame(root, padx=20, pady=20)
        preferencesFrame.pack(side="top", anchor="nw")

        veganInt = tk.IntVar()
        vegan = tk.Checkbutton(preferencesFrame, text="Vegan", font=font.Font(family="Arial", size=20),
                               variable=veganInt)
        vegan.pack(side="left", padx=20)

        vegetarianInt = tk.IntVar()
        vegetarian = tk.Checkbutton(preferencesFrame, text="Vegetarian", font=font.Font(family="Arial", size=20),
                                    variable=vegetarianInt)
        vegetarian.pack(side="left", padx=20)

        halalInt = tk.IntVar()
        halal = tk.Checkbutton(preferencesFrame, text="Halal", font=font.Font(family="Arial", size=20),
                               variable=halalInt)
        halal.pack(side="left", padx=20)

        allergiesLabel = ttk.Label(root, text="Allergies:", bootstyle="solar",
                                   font=font.Font(family="Arial", size=34))
        allergiesLabel.pack(side="top", anchor="nw", padx=40, pady=10)

        allergiesFrame = tk.Frame(root, padx=20, pady=20)
        allergiesFrame.pack(side="top", anchor="nw")

        dairyInt = tk.IntVar()
        dairy = tk.Checkbutton(allergiesFrame, text="Dairy", font=font.Font(family="Arial", size=20), variable=dairyInt)
        dairy.pack(side="left", padx=20)

        eggInt = tk.IntVar()
        egg = tk.Checkbutton(allergiesFrame, text="Egg", font=font.Font(family="Arial", size=20), variable=eggInt)
        egg.pack(side="left", padx=20)

        wheatInt = tk.IntVar()
        wheat = tk.Checkbutton(allergiesFrame, text="Wheat", font=font.Font(family="Arial", size=20), variable=wheatInt)
        wheat.pack(side="left", padx=20)

        sesameInt = tk.IntVar()
        sesame = tk.Checkbutton(allergiesFrame, text="Sesame", font=font.Font(family="Arial", size=20),
                                variable=sesameInt)
        sesame.pack(side="left", padx=20)

        cornInt = tk.IntVar()
        corn = tk.Checkbutton(allergiesFrame, text="Corn", font=font.Font(family="Arial", size=20), variable=cornInt)
        corn.pack(side="left", padx=20)

        soyInt = tk.IntVar()
        soy = tk.Checkbutton(allergiesFrame, text="Soy", font=font.Font(family="Arial", size=20), variable=soyInt)
        soy.pack(side="left", padx=20)

        coconutInt = tk.IntVar()
        coconut = tk.Checkbutton(allergiesFrame, text="Coconut", font=font.Font(family="Arial", size=20),
                                 variable=coconutInt)
        coconut.pack(side="left", padx=20)

        nutsInt = tk.IntVar()
        nuts = tk.Checkbutton(allergiesFrame, text="Nuts", font=font.Font(family="Arial", size=20), variable=nutsInt)
        nuts.pack(side="left", padx=20)

        fishInt = tk.IntVar()
        fish = tk.Checkbutton(allergiesFrame, text="Fish", font=font.Font(family="Arial", size=20), variable=fishInt)
        fish.pack(side="left", padx=20)

        milkInt = tk.IntVar()
        milk = tk.Checkbutton(allergiesFrame, text="Milk", font=font.Font(family="Arial", size=20), variable=milkInt)
        milk.pack(side="left", padx=20)

        submitButton = ttk.Button(root, text="Submit", bootstyle="info-toolbutton",
                                  command=lambda: submit(minCaloriesEntry, maxCaloriesEntry, minProteinEntry,
                                                         maxProteinEntry))
        submitButton.pack(side="left", padx=40)
        root.mainloop()


