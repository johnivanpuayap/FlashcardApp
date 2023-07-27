from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


# Window
window = Tk()
window.config(bg=BACKGROUND_COLOR)
window.title("Flashy")
window.config(pady=50, padx=50)

# Card

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image_front_card = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=image_front_card)
text_french = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, 'italic'))
text_word = canvas.create_text(400, 263, text="trouve", fill="black", font=("Ariel", 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# button_front_card = Button(image=image_front_card, height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
# button_front_card.grid(column=0, row=0, columnspan=2)

# image_back_card = PhotoImage(file="images/card_back.png")
# button_back_card = Button(image=image_back_card)

image_right = PhotoImage(file="images/right.png")
button_check = Button(image=image_right, highlightthickness=0, bg=BACKGROUND_COLOR)
button_check.grid(column=1, row=1)

image_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, bg=BACKGROUND_COLOR)
button_wrong.grid(column=0, row=1)

# Labels



window.mainloop()