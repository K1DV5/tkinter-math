tkinter-math
=====

Render math on Tkinter canvas

- Free software: MIT license

tkinter-math is a library to render math on a Tkinter canvas. It is made for docal but making it
work with at least with MathML is straightforward and is planned to be implemented.

tkinter-math permits you to easily render mathematical equations on a tkinter canvas,
it's core module provide the main feutures documented [here](./docs). But if you just
want to display a custom equation `tkinter_math` provide wrapper classes to make
the process some easier:

```python
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
        Frac(Plus(1, Sqrt(5)),2),
        "n",
      ),
      Pow(
        Frac(Minus(1, Sqrt(5)),2),
        "n",
      ),
    ),
  )
)

fib_nth_term.render(canvas)

root.mainloop()
```
![](examples\fibonacci_nth.png)

And that's it!. You could read more about this in the docs at [./docs](./docs)
