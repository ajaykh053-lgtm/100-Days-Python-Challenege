from tkinter import *
import pandas
import random

FONT_NAME = "Ariel"
BAGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pandas.read_csv("day31/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("day31/data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
finally:
    to_learn = data.to_dict(orient="records")


# ----------------------------------------WORKING-----------------------------------------#
def next_card():
    global current_card, flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_image, image=old_image)
    canvas.itemconfig(title, text="French", fill="Black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="Black")
    flip_timmer = window.after(3000, func=flip_card)


# -------------------------------------FLIPPING CARD---------------------------------------#
def flip_card():
    global current_card
    canvas.itemconfig(canvas_image, image=new_image)
    canvas.itemconfig(title, text="English", fill="White")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="White")


# -----------------------------------SAVIGN YOUR PROGRESS ---------------------------------#
def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("day31/data/words_to_learn.csv", index=False)
    next_card()


# ------------------------------------------UI--------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(width=1100, height=900, bg=BAGROUND_COLOR, padx=50, pady=50)
flip_timmer = window.after(3000, func=flip_card)
# Canvas Front page
canvas = Canvas(width=800, height=526, bg=BAGROUND_COLOR, highlightthickness=0)
old_image = PhotoImage(file="day31/images/card_front.png")
new_image = PhotoImage(file="day31/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=old_image)

# text on canvas
title = canvas.create_text(
    390, 150, text="", fill="Black", font=("Ariel", 25, "italic")
)
word = canvas.create_text(390, 263, text="", fill="Black", font=("Ariel", 40, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons

cross_image = PhotoImage(file="day31/images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card, bg=BAGROUND_COLOR
)
unknown_button.grid(row=1, column=0)

chechmark_image = PhotoImage(file="day31/images/right.png")
known_button = Button(
    image=chechmark_image, highlightthickness=0, command=is_known, bg=BAGROUND_COLOR
)
known_button.grid(row=1, column=1)
next_card()
window.mainloop()
