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
        # root = Tk()
        # root.title("Ologically Speaking: The Ultimate Quiz")

        root.columnconfigure(0, weight=1)

        # Create the heading frame
        self.heading_frame = Frame(root)
        self.heading_frame.grid(row=0, column=0, pady=10)

        # Add the heading label
        self.heading_label = Label(self.heading_frame, text="Ologically Speaking: The Ultimate Quiz",
                                   font=("Helvetica", 16, "bold"))
        self.heading_label.pack()

        # Create the description frame
        self.description_frame = Frame(root)
        self.description_frame.grid(row=1, column=0, pady=10)

        # Add the description label
        self.description_label = Label(self.description_frame, text=(
            "Welcome to the ultimate Ology quiz! In this quiz you will be asked questions about what "
            "specific ology's are and what they are the study of. You'll have 4 different answers to choose from.\n\n"
            "Enter the amount of rounds you'd like and hit Go! (or you can choose infinite and go until your heart's "
            "content)"),
                                       wraplength=400)
        self.description_label.pack()

        # Create the question frame
        self.question_frame = Frame(root)
        self.question_frame.grid(row=2, column=0, pady=10)

        # Add the "How many questions?" label and entry
        self.questions_label = Label(self.question_frame, text="How many questions?",
                                     font=("Arial", 12))
        self.questions_label.grid(row=0, column=0, padx=10)

        self.questions_entry = Entry(self.question_frame)
        self.questions_entry.grid(row=0, column=1, padx=10)

        # Add the "Go" button
        self.go_button = Button(self.question_frame, fg=button_fg,
                                bg="#CC0000", text="Go",
                                font=button_font, width=10,
                                command=lambda: self.check_no_answers()
                                )
        self.go_button.grid(row=0, column=2, padx=5, pady=5)

    def check_no_answers(self):
        print("checking answers??")
        has_error = "no"
        error = "Please enter a number that is more than {}".format(0)

        # Check that user has entered a valid number
        response = self.questions_entry.get()

        try:
            response = int(response)  # Changed to int since we want whole numbers
            if response <= 0:
                has_error = "yes"
        except ValueError:
            has_error = "yes"

        # Set error message if there is an error
        if has_error == "yes":
            print("houston we have a problem")
            self.output_answer("Please enter a valid positive number.")
            self.var_has_errors.set("yes")
        else:
            self.var_has_errors.set("no")
            self.to_play(response)

        output = self.var_feedback.get()
        has_errors = self.var_has_errors.get()

        print("has errors", has_errors)

        if has_errors == "yes":
            # red text, pink entry box
            self.questions_label.config(fg="#9C0000")
            self.questions_entry.config(bg="#F8CECC")

        else:
            self.questions_label.config(fg="#004C00")
            self.questions_entry.config(bg="#FFFFFF")

        self.questions_label.config(text=output)

    def to_play(self, how_many):
        Play(how_many)


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

        self.user_scores = []

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        rounds_heading = "Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        instructions = "{} is the study of?"
        self.instructions_label = Label(self.quest_frame, text=instructions,
                                        wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=3)

        self.first_choice_button = Button(self.choice_frame, text="Option 1:",
                                          fg="#FFFFFF", bg="#008BFC",
                                          font=("Arial", 11, "bold"),
                                          width=10)

        for item in range(1, 4):
            self.choice_button = Button(self.choice_frame,
                                        width=15,
                                        command=lambda: self
                                        )
            self.choice_button.grid(row=3,
                                    padx=5, pady=5)

        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=4)

        for item in range(1, 4):
            self.choice_button = Button(self.choice_frame,
                                        width=15,
                                        command=lambda: self
                                        )
            self.choice_button.grid(row=4,
                                    padx=5, pady=5)

        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=5)

        for item in range(1, 4):
            self.choice_button = Button(self.choice_frame,
                                        width=15,
                                        command=lambda: self
                                        )
            self.choice_button.grid(row=5,
                                    padx=5, pady=5)

        self.choice_frame = Frame(self.quest_frame)
        self.choice_frame.grid(row=6)

        for item in range(1, 4):
            self.choice_button = Button(self.choice_frame,
                                        width=15,
                                        command=lambda: self
                                        )
            self.choice_button.grid(row=6,
                                    padx=5, pady=5)

            # frame to include round results and next button
            self.rounds_frame = Frame(self.quest_frame)
            self.rounds_frame.grid(row=7, pady=5)

            self.next_button = Button(self.rounds_frame, text="Next Round",
                                      fg="#FFFFFF", bg="#008BFC",
                                      font=("Arial", 11, "bold"),
                                      width=10, state=DISABLED,
                                      command=self.new_round)
            self.next_button.grid(row=7)

            # at start, get 'new round'
            self.new_round()

    def get_all_questions(self):
        file = open("study_of.csv", "r")
        var_all_questions = list(csv.reader(file, delimiter=","))
        file.close()

        # removes first entry in list (ie: the header row).
        var_all_questions.pop(0)
        return var_all_questions

    def new_round(self):

        # disable next button (renable it at the end
        # of the round)
        self.next_button.config(state=DISABLED)

    def close_play(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz thingy")
    ChooseRounds()
    root.mainloop()
