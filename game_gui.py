from tkinter import *
from functools import partial  # To prevent unwanted windows
import csv
import random

class ChooseRounds:

    def __init__(self):
        button_fg = "#FFFFFF"
        button_font = ("Arial", "13", "bold")

        self.var_feedback = StringVar()
        self.var_feedback.set("no")

        self.var_has_errors = StringVar()
        self.var_has_errors.set("no")

        # Create the main window
        root = Tk()
        root.title("Ologically Speaking: The Ultimate Quiz")

        root.columnconfigure(0, weight=1)

        # Create the heading frame
        heading_frame = Frame(root)
        heading_frame.grid(row=0, column=0, pady=10)

        # Add the heading label
        heading_label = Label(heading_frame, text="Ologically Speaking: The Ultimate Quiz",
                              font=("Helvetica", 16, "bold"))
        heading_label.pack()

        # Create the description frame
        description_frame = Frame(root)
        description_frame.grid(row=1, column=0, pady=10)

        # Add the description label
        description_label = Label(description_frame, text=(
            "Welcome to the ultimate Ology quiz! In this quiz you will be asked questions about what "
            "specific ology's are and what they are the study of. You'll have 4 different answers to choose from.\n\n"
            "Enter the amount of rounds you'd like and hit Go! (or you can choose infinite and go until your heart's "
            "content)"),
                                  wraplength=400)
        description_label.pack()

        # Create the question frame
        self.question_frame = Frame(root)
        self.question_frame.grid(row=2, column=0, pady=10)

        # Add the "How many questions?" label and entry
        questions_label = Label(self.question_frame, text="How many questions?", font=("Arial", 12))
        questions_label.grid(row=0, column=0, padx=10,)

        questions_entry = Entry(self.question_frame)
        questions_entry.grid(row=0, column=1, padx=10)

        # Add the "Go" button
        self.go_button = Button(self.question_frame, fg=button_fg,
                                bg="#CC0000", text="Go",
                                font=button_font, width=10,
                                command=lambda: self.to_play(0)
                                )
        self.go_button.grid(row=0, column=2, padx=5, pady=5)


    def to_play(self, num_questions):
        Play(num_questions)


class Play:

    def __init__(self, how_many):

        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # Variables used to work out statistics, when game ends etc
        self.rounds_wanted = IntVar()
        self.rounds_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.rounds_played = IntVar()
        self.rounds_played.set(0)

        self.rounds_won = IntVar()
        self.rounds_won.set(0)

        print(f"you chose {how_many} questions")


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz thingy")
    ChooseRounds()
    root.mainloop()
