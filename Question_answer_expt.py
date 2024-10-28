import csv
import random

def get_all_questions():
    file = open("study_of.csv", "r")
    var_all_questions = list(csv.reader(file, delimiter=","))
    file.close()

    # removes first entry in list (ie: the header row).
    var_all_questions.pop(0)
    return var_all_questions


all_questions = get_all_questions()
print(all_questions)

question_ans = random.choice(all_questions)
print(question_ans)

# first item of list
question = question_ans[0]

# second item of list
answer = question_ans[1]

print(f"Question: {question}  |  Answer: {answer}")