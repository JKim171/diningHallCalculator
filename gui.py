import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class GUI:
    @staticmethod
    def runGUI():
        root = ttk.Window(title="Dining Hall Calculator", themename="solar", size=(1920, 1080))

        diningHallFrame = tk.Frame(root, padx=20, pady=20)
        diningHallFrame.pack(side="top", anchor="nw")

        diningHallLabel = ttk.Label(diningHallFrame, text="Dining Hall:", bootstyle="solar",
                                    font=font.Font(family="Arial", size=34))
        diningHallLabel.pack(side="top", anchor="nw", padx=20)

        diningHallButtonFrame = tk.Frame(root, padx=20, pady=20)
        diningHallButtonFrame.pack(side="top", anchor="nw")

        rhetasButton = ttk.Button(diningHallButtonFrame, text="Rheta's Market", bootstyle="info-toolbutton")
        rhetasButton.pack(side="left", padx=20)

        gordonButton = ttk.Button(diningHallButtonFrame, text="Gordon Avenue Market", bootstyle="info-toolbutton")
        gordonButton.pack(side="left", padx=20)

        lowellButton = ttk.Button(diningHallButtonFrame, text="Lowell Market", bootstyle="info-toolbutton")
        lowellButton.pack(side="left", padx=20)

        lizButton = ttk.Button(diningHallButtonFrame, text="Liz's Market", bootstyle="info-toolbutton")
        lizButton.pack(side="left", padx=20)

        carsonButton = ttk.Button(diningHallButtonFrame, text="Carson's Market", bootstyle="info-toolbutton")
        carsonButton.pack(side="left", padx=20)

        fourLakesButton = ttk.Button(diningHallButtonFrame, text="Four Lakes Market", bootstyle="info-toolbutton")
        fourLakesButton.pack(side="left", padx=20)

        timeLabelFrame = tk.Frame(root, padx=20, pady=20)
        timeLabelFrame.pack(side="top", anchor="nw")

        timeLabel = ttk.Label(timeLabelFrame, text="Time:", bootstyle="solar",
                              font=font.Font(family="Arial", size=34))
        timeLabel.pack(side="top", anchor="nw", padx=20)

        timeFrame = tk.Frame(root, padx=20, pady=20)
        timeFrame.pack(side="top", anchor="nw")

        breakfastButton = ttk.Button(timeFrame, text="Breakfast", bootstyle="info-toolbutton")
        breakfastButton.pack(side="left", padx=20)

        lunchButton = ttk.Button(timeFrame, text="Lunch", bootstyle="info-toolbutton")
        lunchButton.pack(side="left", padx=20)

        dinnerButton = ttk.Button(timeFrame, text="Dinner", bootstyle="info-toolbutton")
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
        vegan = tk.Checkbutton(preferencesFrame, text="Vegan", font=font.Font(family="Arial", size=20), variable=veganInt)
        vegan.pack(side="left", padx=20)

        vegetarianInt = tk.IntVar()
        vegetarian = tk.Checkbutton(preferencesFrame, text="Vegetarian", font=font.Font(family="Arial", size=20),
                                    variable=vegetarianInt)
        vegetarian.pack(side="left", padx=20)

        halalInt = tk.IntVar()
        halal = tk.Checkbutton(preferencesFrame, text="Halal", font=font.Font(family="Arial", size=20), variable=halalInt)
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
        sesame = tk.Checkbutton(allergiesFrame, text="Sesame", font=font.Font(family="Arial", size=20), variable=sesameInt)
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
        nuts.pack(side="left", padx=20)

        milkInt = tk.IntVar()
        milk = tk.Checkbutton(allergiesFrame, text="Milk", font=font.Font(family="Arial", size=20), variable=milkInt)
        milk.pack(side="left", padx=20)

        submitButton = ttk.Button(root, text="Submit", bootstyle="info-toolbutton")
        submitButton.pack(side="left", padx=40)

        root.mainloop()