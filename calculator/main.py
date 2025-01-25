from tkinter import *
from calculation import solve

window = Tk()
window.title("Calculator")
window.minsize(height=100, width=100)

label = Label(text="", anchor="w", height=2, font=("Atria",20, "bold"))
label.grid(column=0, row=0, columnspan=4, sticky="we")

val = ""

def change_name(n):
    global val
    if not 47 < ord(n) < 58:
        num = len(val) - 1
        if ord(val[num]) in (42, 43, 47, 45) :
            val = val[:num] + n
        else:
            val = val + n
    else:
        val = val + n
    label.config(text=val)

def clear():
    global val
    label.config(text="")
    val = ""

def calculate():
    global val
    val = str(solve(val))
    label.config(text=val)

button_1 = Button(text="1", command=lambda: change_name("1"), height=1, width=1)
button_1.grid(column = 0, row = 1)

button_2 = Button(text="2", command=lambda: change_name("2"), height=1, width=1)
button_2.grid(column = 1, row = 1)

button_3 = Button(text="3", command=lambda: change_name("3"), height=1, width=1)
button_3.grid(column = 2, row = 1)

button_4 = Button(text="4", command=lambda: change_name("4"), height=1, width=1)
button_4.grid(column = 0, row = 2)

button_5 = Button(text="5", command=lambda: change_name("5"), height=1, width=1)
button_5.grid(column = 1, row = 2)

button_6 = Button(text="6", command=lambda: change_name("6"), height=1, width=1)
button_6.grid(column = 2, row = 2)

button_7 = Button(text="7", command=lambda: change_name("7"), height=1, width=1)
button_7.grid(column = 0, row = 3)

button_8 = Button(text="8", command=lambda: change_name("8"), height=1, width=1)
button_8.grid(column = 1, row = 3)

button_9 = Button(text="9", command=lambda: change_name("9"), height=1, width=1)
button_9.grid(column = 2, row = 3)

button_0 = Button(text="0", command=lambda: change_name("0"), height=1, width=1)
button_0.grid(column = 1, row = 4)

button_plus = Button(text="+", command=lambda: change_name("+"), height=1, width=1)
button_plus.grid(column = 3, row = 4)

button_minus = Button(text="-", command=lambda: change_name("-"), height=1, width=1)
button_minus.grid(column = 3, row = 3)

button_multi = Button(text="*", command=lambda: change_name("*"), height=1, width=1)
button_multi.grid(column = 3, row = 2)

button_div = Button(text="/", command=lambda: change_name("/"), height=1, width=1)
button_div.grid(column = 3, row = 1)

button_equal = Button(text="=", command= calculate, height=1, width=1)
button_equal.grid(column = 2, row = 4)

button_ac = Button(text="AC", command= clear, height=1, width=1)
button_ac.grid(column = 0, row = 4)

window.mainloop()