import sqlite3
import tkinter as tkinter

conn = sqlite3.connect("music.sqlite")


class Scrollbox(tkinter.Listbox):
    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(
            window, orient=tkinter.VERTICAL, command=self.yview
        )

    def grid(self, row, column, sticky="nsw", rowspan=1, columnspan=1, **kwargs):
        super().grid(
            row=row,
            column=column,
            sticky=sticky,
            rowspan=rowspan,
            columnspan=columnspan,
            **kwargs
        )  # noqa
        self.scrollbar.grid(row=row, column=column, sticky="nse", rowspan=rowspan)
        self["yscrollcommand"] = self.scrollbar.set


# I'm going to to need three columns
# I'm going to need two rows
# I will all together four rows

mainWindow = tkinter.Tk()
mainWindow.title("Music DB Browser")
mainWindow.geometry("1024x768")

mainWindow.columnconfigure(0, weight=2)
mainWindow.columnconfigure(1, weight=2)
mainWindow.columnconfigure(2, weight=2)
mainWindow.columnconfigure(3, weight=1)  # spacer column on right

mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=5)
mainWindow.rowconfigure(2, weight=5)
mainWindow.rowconfigure(3, weight=1)

# ======= labels =======
tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

# ======= Artists Listbox =======
artistList = Scrollbox(mainWindow, background="red")
artistList.grid(row=1, column=0, sticky="nsew", rowspan=2, padx=(30, 0))
artistList.config(border=2, relief="sunken")

for artist in conn.execute("SELECT artists.name From artists ORDER BY artists.name"):
    artistList.insert(tkinter.END, artist[0])

# ======= Albums Listbox =======
albumLV = tkinter.Variable(mainWindow)
albumLV.set(("Choose An Album",))
albumList = Scrollbox(mainWindow, listvariable=albumLV)
albumList.grid(row=1, column=1, sticky="nsew", padx=(30, 0))
albumList.config(border=2, relief="sunken")

# ======= Songs Listbox =======
songLV = tkinter.Variable(mainWindow)
songLV.set(("Choose A Song",))
songList = Scrollbox(mainWindow, listvariable=songLV, background="light blue")
songList.grid(row=1, column=2, sticky="nsew", padx=(30, 0))
songList.config(border=2, relief="sunken")

# ======= Main Loop =======
testList = range(0, 100)
albumLV.set(tuple(testList))
mainWindow.mainloop()
print("Closing database connection")
conn.close()
