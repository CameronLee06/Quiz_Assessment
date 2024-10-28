def check_no_answers(self):
    has_error = "no"
    error = "Please enter a number that is more " \
            "than {}".format(0)

    # check that user has entered a valid number...

    response = self.temp_entry.get()

    try:
        response = float(response)

        if response < 0:
            has_error = "yes"

    except ValueError:
        has_error = "yes"

    # Sets var_has_error so that entry box and
    # labels can be correctly formatted by formatting function
    if has_error == "yes":
        self.var_has_errors.set("yes")
        self.var_feedback.set(error)
        return "invalid"

    # If we have no error...
    else:
        # set to 'no' in case of previous errors
        self.var_has_errors.set("no")


def output_answer(self):
    output = self.var_feedback.get()
    has_errors = self.var_has_errors.get()

    print("has errors", has_errors)

    if has_errors == "yes":
        # red text, pink entry box
        self.output_label.config(fg="#9C0000")
        self.temp_entry.config(bg="#F8CECC")

    else:
        self.output_label.config(fg="#004C00")
        self.temp_entry.config(bg="#FFFFFF")

    self.output_label.config(text=output)
