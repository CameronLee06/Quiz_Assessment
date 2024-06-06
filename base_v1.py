from tkinter import *
from functools import partial # To prevent unwanted windows
import csv
import random


# users choose 2, 4, or 6 rounds

class ChooseRounds:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        # Set up GUI Frame
        self.intro_frame = Frame(padx=10, pady=10)
        self.intro_frame.grid()

        # heading and brief instructions
        self.intro_heading_label = Label(self.intro_frame,
                                         text="Ologies Quiz",
                                         font=("Arial", "16", "bold"))
        self.intro_heading_label.grid(row=0)

        instructions_txt = "You will choose between "