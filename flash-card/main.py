import time
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

words = pd.read_csv("data/Hindi-English.csv")
data = words.to_dict(orient="records")
current_card = {}

def right():
    next_card()
    data.remove(current_card)

def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(data)
    canvas.itemconfig(word, text=current_card["Hindi"], fill="Black")
    canvas.itemconfig(title, text="Hindi", fill="Black")
    canvas.itemconfig(card_background, image=front)
    timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(card_background, image=back)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)

front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")
correct = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(height=526,width=800,highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400,263,image=front)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word  = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

next_card()

true = Button(image=correct, command=right, bg=BACKGROUND_COLOR)
true.grid(column = 0, row = 1)

false = Button(image=wrong, command=next_card, bg=BACKGROUND_COLOR)
false.grid(column = 1, row = 1)

window.mainloop()

qwerty = pd.DataFrame(data)
qwerty.to_csv("data/Hindi-English.csv")