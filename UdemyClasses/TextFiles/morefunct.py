""" Import a the tkinter module to create a parablola
:return: import tkinter as Tkinter
:rtype: also expressing a try statement
"""

try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter


def parablola(x):
    y = x * x
    return y


def draw_axes(_canvas):
    canvas.update()
    x_origin = canvas.winfo_width() / 2
    y_origin = canvas.winfo_height() / 2
    canvas.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    canvas.create_line(-x_origin, 0, x_origin, 0, fill="black")
    canvas.create_line(0, y_origin, 0, -y_origin, fill="black")


def plot(canvas, x, y):
    canvas.create_line(x, y, x + 1, fill="red")


mainWindow = tkinter.Tk()

mainWindow.title("Parablola")
mainWindow.geometry("640x480")

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)

for x in range(-100, 100):
    y = parablola(x)
    plot(canvas, x, y)

mainWindow.mainloop()
