""" Import a the tkinter module to create a parablola
:return: import tkinter as Tkinter
:rtype: also expressing a try statement
"""

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parablola(n):
    s = n * n
    return s


def draw_anes(_canvas):
    canvas.update()
    n_origin = canvas.winfo_width() / 2
    s_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-n_origin, -s_origin, n_origin, s_origin))
    _canvas.create_line(-n_origin, 0, -s_origin, fill="white")


def plot(_canvas, n, s):
    canvas.create_line(n, s, n + 1, s + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parablola")
mainWindow.geometry("640n480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_anes(canvas)

for n in range(-100, 100):
    s = parablola(n)
    plot(canvas, n, s)

mainWindow.mainloop()
