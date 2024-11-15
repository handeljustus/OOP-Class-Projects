import tkinter as tk
from tkinter import *


box = Tk ()

box.geometry ("1000x1000")

answer = Text (width=60, height=5, bg="black", fg="white")
answer.place (x = 100, y = 100)

def display (x):

    if x == "=":
        final_answer = eval(answer.get(1.0, "end-1c"))
        answer.insert (tk.INSERT, x)
        answer.insert (tk.INSERT, final_answer)

    else:
            answer.insert (tk.INSERT, x)

B1 = Button(box, text="1", width=10, height=5, command=lambda: display("1"))
B1.place(x=100, y=150)
B2 = Button(box, text="2", width=10, height=5, command=lambda: display("2"))
B2.place(x=200, y=150)
B3 = Button(box, text="3", width=10, height=5, command=lambda: display("3"))
B3.place(x=300, y=150)

B4 = Button(box, text="4", width=10, height=5, command=lambda: display("4"))
B4.place(x=100, y=250)
B5 = Button(box, text="5", width=10, height=5, command=lambda: display("5"))
B5.place(x=200, y=250)
B6 = Button(box, text="6", width=10, height=5, command=lambda: display("6"))
B6.place(x=300, y=250)
B7 = Button(box, text="7", width=10, height=5, command=lambda: display("7"))
B7.place(x=100, y=350)
B8 = Button(box, text="8", width=10, height=5, command=lambda: display("8"))
B8.place(x=200, y=350)
B9 = Button(box, text="9", width=10, height=5, command=lambda: display("9"))
B9.place(x=300, y=350)

B10 = Button(box, text="0", width=10, height=5, command=lambda: display("0"))
B10.place(x=200, y=450)
B11 = Button(box, text="+", width=10, height=5, command=lambda: display("+"))
B11.place(x=400, y=150)
B12 = Button(box, text="-", width=10, height=5, command=lambda: display("-"))
B12.place(x=400, y=250)
B13 = Button(box, text="*", width=10, height=5, command=lambda: display("*"))
B13.place(x=400, y=350)

B14 = Button(box, text="=", width=10, height=5, command=lambda: display("="))
B14.place(x=300, y=450)
B15 = Button(box, text="/", width=10, height=5, command=lambda: display("/"))
B15.place(x=400, y=450)
B16 = Button(box, text="Clear", width=7, height=5, command=lambda: answer.delete(1.0, END))
B16.place(x=100, y=450)

box.mainloop()


