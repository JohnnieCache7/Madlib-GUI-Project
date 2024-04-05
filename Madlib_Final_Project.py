""" 
Jonathan Argueta-Herrera
Madlib FINAL PROJECT
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class MadLib:
    def __init__(self, adjective, noun, verb, adverb):
        self.adjective = adjective
        self.noun = noun
        self.verb = verb
        self.adverb = adverb

    def generate_madlib(self):
        raise NotImplementedError("Subclasses must implement generate_madlib")

#Inherited from parent Madlib, displays finished madlib
class SimpleMadLib(MadLib):
    def generate_madlib(self):
        return f"The {self.adjective} {self.noun} {self.verb}s {self.adverb} and makes everyone laugh."

#Inherited from parent Madlib, displays finished madlib
class FunnyMadLib(MadLib):
    def generate_madlib(self):
        return f"In a {self.adjective} land, a group of {self.noun}s decided to {self.verb} {self.adverb} every day."

#takes in user input and choice of madlib
def submit():
    try:
        adjective = adjective_entry.get()
        noun = noun_entry.get()
        verb = verb_entry.get()
        adverb = adverb_entry.get()

        if not adjective or not noun or not verb or not adverb:
            raise ValueError("Please fill in all fields")

        madlib_type = madlib_type_var.get()

        if madlib_type == "Simple":
            madlib = SimpleMadLib(adjective, noun, verb, adverb)
        elif madlib_type == "Funny":
            madlib = FunnyMadLib(adjective, noun, verb, adverb)
        else:
            raise ValueError("Invalid Mad Lib type selected")

        madlib_result = madlib.generate_madlib()

        #get current time
        current_datetime = datetime.now()

        #store madlib and datetime in a list
        madlib_history.append((madlib_result, current_datetime))

        result_label.config(text = madlib_result)

    except ValueError as error:
        messagebox.showerror("Error", str(error))

#clears users input from boxes
def clear_entries():
    adjective_entry.delete(0, tk.END)
    noun_entry.delete(0, tk.END)
    verb_entry.delete(0, tk.END)
    adverb_entry.delete(0, tk.END)
    result_label.config(text = "")

#displays datetime and previous madlibs
def show_history():
    history_text = ""
    for madlib, timestamp in madlib_history:
        history_text += f"{timestamp}: {madlib}\n"
    messagebox.showinfo("Mad Lib History", history_text)


#setting up
madlib_gui = tk.Tk()
madlib_gui.title("Mad Lib")

#gui labels
adjective_label = tk.Label(madlib_gui, text="Adjective:")
noun_label = tk.Label(madlib_gui, text="Noun:")
verb_label = tk.Label(madlib_gui, text="Verb:")
adverb_label = tk.Label(madlib_gui, text="Adverb:")
result_label = tk.Label(madlib_gui, text="")

#user entries
adjective_entry = tk.Entry(madlib_gui)
noun_entry = tk.Entry(madlib_gui)
verb_entry = tk.Entry(madlib_gui)
adverb_entry = tk.Entry(madlib_gui)

#dropdown for the type of madlib
madlib_type_var = tk.StringVar()
madlib_type_var.set("Simple")
madlib_type_label = tk.Label(madlib_gui, text="Mad Lib Type:")
madlib_type_menu = tk.OptionMenu(madlib_gui, madlib_type_var, "Simple", "Funny")

#buttons
submit_button = tk.Button(madlib_gui, text="Generate Mad Lib", command = submit)
clear_button = tk.Button(madlib_gui, text="Clear Entries", command = clear_entries)
history_button = tk.Button(madlib_gui, text="Show History", command = show_history)

#grid layout
adjective_label.grid(row=0, column=0)
noun_label.grid(row=1, column=0)
verb_label.grid(row=2, column=0)
adverb_label.grid(row=3, column=0)
madlib_type_label.grid(row=4, column=0)

adjective_entry.grid(row=0, column=1)
noun_entry.grid(row=1, column=1)
verb_entry.grid(row=2, column=1)
adverb_entry.grid(row=3, column=1)
madlib_type_menu.grid(row=4, column=1)

submit_button.grid(row=5, column=0)
clear_button.grid(row=6, column=0)
history_button.grid(row=7, column=0)
result_label.grid(row=8, column=0, columnspan=2)

#storing the madlib stories
madlib_history = []

#run
madlib_gui.mainloop()
