from tkinter import *

from tkinter_math.math import *

root = Tk()
canvas = Canvas(root, width=500, height=150)
canvas.pack()

set_font(family="Arial", size=20)  # Select font for displaying equations

math = Sigma(
    Minus(
        Pow(
            Frac(Plus(1, Sqrt(5)), 2),
            "n",
        ),
        Pow(
            Frac(Minus(1, Sqrt(5)), 2),
            "n",
        ),
    ),
    "3",
)

math.render(canvas)

root.mainloop()
