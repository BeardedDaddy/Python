"""The line below imports the sqlite3 module."""
import sqlite3
import tkinter

conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):
    """This class creates a function called Scrollbox with the method called tkinter.Listbox."""  # noqa
    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs) # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL, command=self.yview)  # noqa


    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):  # noqa
        """This line creates a function called grid that has several arguments."""  # noqa
        # tkinter.Listbox.gridself, row=row, column=column, sticky=sticky, rowspan=rowspan, **kwargs) # Python 2  # noqa
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)  # noqa
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)  # noqa
        self['yscrollcommand'] = self.scrollbar.set


mainWindow = tkinter.Tk()
mainWindow.title('Music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=2)  # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ===== labels =====
tkinter.Label(mainWindow, text="Artist").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ===== Artists Listbox =====
artistList = Scrollbox(mainWindow, background="green")
artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
artistList.config(border=2, relief='sunken')

# ===== Albums Listbox =====
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose an artist",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
albumList.config(border=2, relief='sunken')

# ===== Songs Listbox =====
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose an album",))
songList = Scrollbox(mainWindow, listvariable=songLV)
songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
songList.config(border=2, relief='sunken')

# ===== Main Loop =====
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("closing database connection")
conn.close()
