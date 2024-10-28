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
            "Enter the amount of rounds you'd like and hit Go!"),
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

    def to_play(self, num_questions):
        Play(num_questions)

        # Hide root window (ie: hide rounds choice window).
        root.withdraw()


class Play:

    def __init__(self, how_many):
        self.play_box = Toplevel()

        # If users press cross at top, closes help and
        # 'releases' help button
        self.play_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_play))

        # Variables used to work out statistics, when game ends etc
        self.questions_wanted = IntVar()
        self.questions_wanted.set(how_many)

        # Initially set rounds played and rounds won to 0
        self.questions_played = IntVar()
        self.questions_played.set(0)

        self.questions_correct = IntVar()
        self.questions_correct.set(0)

        self.stored_correct_answer = StringVar()

        self.user_score = []

        self.user_answer = []

        self.all_questions = self.get_all_questions()

        self.quest_frame = Frame(self.play_box, padx=10, pady=10)
        self.quest_frame.grid()

        self.rounds_heading = Label(self.quest_frame, text=f"Round 1 of".format(how_many),
                                    font=("Arial", "16", "bold"))
        self.rounds_heading.grid(row=0)

        instructions = "{} is the study of?"
        self.instructions_label = Label(self.quest_frame, text=instructions,
                                        wraplength=350, justify="left")
        self.instructions_label.grid(row=1)

        self.button_question_list = []

        self.quest_button_ref = []
        self.all_answers = []

        for item in range(0, 4):
            self.quest_button = Button(self.quest_frame,
                                       width=28, wraplength=150,
                                       command=lambda i=item:
                                       self.to_compare(self.all_answers[i])
                                       )
            self.quest_button.grid(row=item + 2,
                                   padx=5, pady=5)

            # add button to reference list for later configuration
            self.quest_button_ref.append(self.quest_button)

        self.next_button = Button(self.quest_frame, text="Next Round",
                                  fg="#FFFFFF", bg="#CC45CC",
                                  font=("Arial", 11, "bold"),
                                  width=10, state=DISABLED,
                                  command=self.new_round)
        self.next_button.grid(row=7)

        self.question_results_label = Label(self.quest_frame, text="User Score:",
                                            width=32, bg="#FFF2CC",
                                            font=("Arial", 10),
                                            pady=5)
        self.question_results_label.grid(row=8, column=0, padx=5)

        rounds_heading = "Choose - Round 1 of {}".format(how_many)
        self.choose_heading = Label(self.quest_frame, text=rounds_heading,
                                    font=("Arial", "16", "bold")
                                    )
        self.choose_heading.grid(row=0)

        # at start, get 'new round'
        self.new_round()

    def to_compare(self, user_choice):

        how_many = self.questions_wanted.get()
        correct_ans = self.stored_correct_answer.get()

        # Add one to number of rounds played
        current_question = self.questions_played.get()
        current_question += 1
        self.questions_correct.set(current_question)

        # deactivate colour buttons!
        for item in self.quest_button_ref:
            item.config(state=DISABLED)

            win_colour = "#D5E8D4"
            lose_colour = "#F8CECC"

        if current_question == how_many:
            self.next_button.config(state=DISABLED)
            self.next_button['text'] = "Play Again"

            # change all colour button background to light grey
            for item in self.quest_button_ref:
                item['bg'] = "#C0C0C0"

        else:
            # enable next round button and update heading
            self.next_button.config(state=NORMAL)

            if correct_ans == user_choice:
                current_score = self.questions_played.get() + 1
                self.questions_correct.set(current_score)
                question_results_bg = win_colour
                print("yay!")
            else:
                question_results_bg = lose_colour
                print("you loser!")

            user_score = int(current_question)
            self.user_score.append(user_score)

            if user_score == self.stored_correct_answer:
                self.question_results_label.config(bg=win_colour)
            else:
                self.question_results_label.config(bg=lose_colour)

                rounds_outcome_txt = f"Your Score: {self.questions_correct.get()} / {how_many}"

                self.question_results_label.config(bg=question_results_bg,
                                                   text=rounds_outcome_txt)

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

        question_ans = random.choice(self.all_questions)
        question = question_ans[0]
        correct_answer = question_ans[1]
        self.stored_correct_answer.set(correct_answer)

        how_many = self.questions_wanted.get()
        current_round = self.questions_played.get()
        rounds_heading = "User Score: Round {} of " \
                         "{}".format(current_round + 1, how_many)
        self.choose_heading.config(text=rounds_heading)

        self.all_answers = [correct_answer]

        while len(self.all_answers) < 4:
            # choose another question / answer pair
            incorrect_question = random.choice(self.all_questions)

            # if we chose a pair that does not have the right answer, add
            # the wrong answer to the list of choices
            if incorrect_question[1] != correct_answer:
                self.all_answers.append(incorrect_question[1])

        random.shuffle(self.all_answers)

        # second item of list
        print(self.all_answers)

        # puts text on the buttons
        count = 0
        for item in self.quest_button_ref:
            item['text'] = self.all_answers[count]
            item['state'] = NORMAL

            count += 1

        print(f"Question: {question}  |  Answer: {correct_answer}")

        self.next_button.config(state=DISABLED)
        self.next_button.config(bg="#ffff00")

        self.instructions_label.config(text=f"What is {question}?",
                                       font=("Arial", 20),
                                       pady=5)

        if self.questions_played.get() >= self.questions_wanted.get():
            self.question_results_label.config(text="Well Done, You finished.")

    def close_play(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Quiz thingy")
    ChooseRounds()
    root.mainloop()
