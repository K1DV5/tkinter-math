from tkinter import *
from tkinter import font

from tkinter_math.math import *


def render_math(canv: Canvas):
    select_font(font.Font(family="Arial", size=30))
    Eq(3, 5).render(canv)


root = Tk()
canv = Canvas(root)
canv.pack()
render_math(canv)
root.mainloop()
