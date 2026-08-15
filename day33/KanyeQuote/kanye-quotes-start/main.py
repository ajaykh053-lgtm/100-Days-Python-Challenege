from tkinter import Tk, Canvas, PhotoImage, Button,Label
import requests


def get_quote():
    Respones = requests.get(url="https://api.kanye.rest")
    Quote = Respones.json()["quote"]
    canvas.itemconfig(quote_text, text=f"My Nigga says,\n{Quote}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day33/KanyeQuote/kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    text="Nigga Quote Goes HERE",
    width=250,
    font=("Arial", 20, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)
kanye_img = PhotoImage(file="day33/KanyeQuote/kanye-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)
kanye_name = Label(text="My Nigga",font=("Arial", 10, "bold"),highlightthickness=0)
kanye_name.grid(row=2,column=0)

window.mainloop()
