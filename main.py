import tkinter as tk
from tkinter import font
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

if __name__ == '__main__':
    root = ttk.Window(title="Dining Hall Calculator", themename="solar", size=(1920,1080))

    diningHallLabel = ttk.Label(root, text="Dining Hall:", bootstyle="solar", font=font.Font(family="Arial", size=34))
    diningHallLabel.pack(side="top", anchor="nw", margin)

    rhetasButton = ttk.Button(root, text="Rheta's Market", style="info")
    rhetasButton.pack(side="top", anchor="nw")

    root.mainloop()

