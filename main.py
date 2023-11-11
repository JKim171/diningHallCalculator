import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

if __name__ == '__main__':
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

    root.mainloop()
