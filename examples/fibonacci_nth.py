from tkinter import *

from tkinter_math.math import *

root = Tk()
canvas = Canvas(root)
canvas.pack()

set_font(family="Arial", size=20)  # Select font for displaying equations

fib_nth_term = Eq(
    "F_n",
    Times(
        Frac(1, Sqrt(5)),
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
    ),
)

fib_nth_term.render(canvas)

root.mainloop()
