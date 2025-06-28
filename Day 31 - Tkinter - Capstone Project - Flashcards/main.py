

from tkinter import *
from tkinter import messagebox
import json
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
   original_data = pandas.read_csv("data/french_words.csv")
   to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
   global current_card, flip_timer
   window.after_cancel(flip_timer)
   current_card = random.choice(to_learn)
   print(current_card["French"])
   canvas.itemconfig(card_title,text="French", fill="black")
   canvas.itemconfig(card_word, text=current_card["French"], fill="black")
   canvas.itemconfig(card_background, image=card_front_img)
   flip_timer = window.after(3000, func=flip_card)



def flip_card():
   canvas.itemconfig(card_title, text="English")
   canvas.itemconfig(card_word, text=current_card["English"])
   canvas.itemconfig(card_background, image=card_back_img)


def is_known():
   to_learn.remove(current_card)
   data = pandas.DataFrame(to_learn)
   data.to_csv("data/words_to_learn.csv",index=False)
   next_card()



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")


canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0,column=0,columnspan=2)

card_title = canvas.create_text(400,150, text="French", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263, text="Partie", font=("Ariel",60,"bold"))

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1,column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1,column=1)


next_card()







window.mainloop()
