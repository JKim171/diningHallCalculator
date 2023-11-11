import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

if __name__ == '__main__':
    root = ttk.Window(title="Dining Hall Calculator", themename="solar", size=(1920, 1080))

    diningHallFrame = tk.Frame(root, padx=20, pady=20)
    diningHallFrame.pack(side="top", anchor="nw")

    diningHallLabel = ttk.Label(diningHallFrame, text="Dining Hall:", bootstyle="solar", font=font.Font(family="Arial", size=34))
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

    root.mainloop()



