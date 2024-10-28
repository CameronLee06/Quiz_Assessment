from tkinter import *

# Create the main window
root = Tk()
root.title("Ologically Speaking: The Ultimate Quiz")


def submit_question():
    question = questions_entry.get()
    print(f"Submitted Question: {question}")
    # Add code here to handle the submitted question (e.g., save it, process it, etc.)


def on_entry_click(event):
    if questions_entry.get() == 'How many questions?':
        questions_entry.delete(0, "end")  # delete all the text in the entry
        questions_entry.insert(0, '')  # insert blank for user input
        questions_entry.config(foreground='black')


def on_focusout(event):
    if questions_entry.get() == '':
        questions_entry.insert(0, 'How many questions?')
        questions_entry.config(foreground='grey')


# Configure the grid to make the infinite button stretch across the screen
root.columnconfigure(0, weight=1)

# Create the heading frame
heading_frame = Frame(root)
heading_frame.grid(row=0, column=0, pady=10)

# Add the heading label
heading_label = Label(heading_frame, text="Ologically Speaking: The Ultimate Quiz", font=("Helvetica", 16, "bold"))
heading_label.pack()

# Create the description frame
description_frame = Frame(root)
description_frame.grid(row=1, column=0, pady=10)

# Add the description label
description_label = Label(description_frame, text=(
    "Welcome to the ultimate Ology quiz! In this quiz you will be asked questions about what "
    "specific ology's are and what they are the study of. You'll have 4 different answers to choose from.\n\n"
    "Enter the amount of rounds you'd like and hit Go! (or you can choose infinite and go until your heart's content)"),
                          wraplength=400)
description_label.pack()

# Create the question frame
question_frame = Frame(root)
question_frame.grid(row=2, column=0, pady=10)

# Add the "How many questions?" label and entry
questions_label = Label(question_frame, text="How many questions?", font=("Arial", 12))
questions_label.grid(row=0, column=0, padx=10)

questions_entry = Entry(question_frame)
questions_entry.insert(0, 'How many questions?')
questions_entry.bind('<FocusIn>', on_entry_click)
questions_entry.bind('<FocusOut>', on_focusout)
questions_entry.grid(row=0, column=1, padx=10)

# Add the "Go" button
go_button = Button(question_frame, text="Go", width=10)  # Adjust the width here
go_button.grid(row=0, column=2, padx=10)

# Add the "Infinite" button
infinite_button = Button(root, text="Infinite", width=20)  # Adjust the width here
infinite_button.grid(row=3, column=0, pady=10)

# Run the application
root.mainloop()
