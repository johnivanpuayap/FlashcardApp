from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
word = ""
data = {}
timer = None


def start_app():
    global timer
    global word
    global data
    word = random.choice(data)
    show_word()
    timer = window.after(5000, flip_card)


def flip_card():
    global word
    canvas.itemconfig(canvas_image, image=image_back_card)
    canvas.itemconfig(text_language, text=f"{'English'}")
    canvas.itemconfig(text_word, text=f"{word['English']}")


def show_word():
    global word
    canvas.itemconfig(canvas_image, image=image_front_card)
    canvas.itemconfig(text_language, text=f"{'French'}")
    canvas.itemconfig(text_word, text=f"{word['French']}")


def change_word():
    global timer
    global word
    global data
    window.after_cancel(timer)
    word = random.choice(data)
    show_word()
    timer = window.after(5000, flip_card)


# Window
window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")
window.config(pady=50, padx=50)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front_card = PhotoImage(file="images/card_front.png")
image_back_card = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=image_front_card)
text_language = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, 'italic'))
text_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
image_right = PhotoImage(file="images/right.png")
button_check = Button(image=image_right, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)
button_check.grid(column=1, row=1)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=change_word)
button_wrong.grid(column=0, row=1)

# Load the Data
data = pd.read_csv("data/french_words.csv")
data = data.to_dict(orient="records")

start_app()

window.mainloop()
