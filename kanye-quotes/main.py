from tkinter import *
import requests

def new_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    kanya_quote = response.json()["quote"]
    canvas.itemconfig(quote_text, text=f"{kanya_quote}")


window = Tk()
window.title("Kanya says")
window.config(padx=50, pady=50)

canvas = Canvas(height=414, width= 300, highlightthickness=0)
background = PhotoImage(file="background.png")
canvas.create_image(150, 207, image= background)
quote_text = canvas.create_text(150, 207, text="hello", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(column=0, row=0, columnspan=3)

kanye_img = PhotoImage(file="kanye.png")
start = Button(image=kanye_img,highlightthickness=0,command=new_quote)
start.grid(column=1,row=1)

new_quote()

window.mainloop()