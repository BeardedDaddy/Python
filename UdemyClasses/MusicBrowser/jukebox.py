""" This module uses the sqlite3 module to interact with a SQLite database.
"""

import sqlite3
import tkinter

conn = sqlite3.connect('music.sqlite')


class Scrollbox(tkinter.Listbox):
    """ Line 10 creates a class called Scrollbox that has method as argument.
    """

    def __init__(self, window, **kwargs):
        # tkinter.Listbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.scrollbar = tkinter.Scrollbar(window, orient=tkinter.VERTICAL,
                                           command=self.yview)

    def grid(self, row, column, sticky='nsw',
             rowspan=1, columnspan=1, **kwargs):
        """ This function creates a grid with the parameters
        of row, column, and sticky.
        """

        # tkinter.Listbox.grid(self, row=row, column=column, sticky=sticky,
        # rowspan=rowspan,
        #  **kwargs)  # Python 2
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan,
                     columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse',
                            rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class DataListBox(Scrollbox):
    """ Line 36 creates a class called DataListBox that has method as argument.
    """
    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):  # noqa
        # Scrollbox.__init__(self, window, **kwargs)  # Python 2
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table  # noqa
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        """clear class, is used to clear the listbox.
        """
        self.delete(0, tkinter.END)

    def requery(self, link_value=None):
        """requery class, is used to requery the listbox.
        """
        if link_value:
            sql = self.sql_select + " WHERE " + "artist" + "=?" + self.sql_sort
            print(sql)   # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])

    def on_select(self, event):
        print(self is event.widget)  # TODO delete this line.
        """ This line of code creates a function called def get_albums()
        with a argument called event.
        """

        index = self.curselection()[0]

        # get the artist name from the listbox
        value = self.get(index),

        # get the artist ID from the database row
        link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]  # noqa
        albumList.requery(link_id)

        # artist_id = conn.execute('SELECT artists._id FROM artists WHERE artists.name=?', artist_name).fetchone()  # noqa
        # alist = []
        # for row in conn.execute('SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name', artist_id):  # noqa
        #     alist.append(row[0])
        # albumLV.set(tuple(alist))
        # songLV.set(("Choose an album",))


def get_songs(event):
    """get_songs is the function name.

    Parameters
    ----------
    event
        This function called get_songs creates a parameter called event.
    """
    lb = event.widget
    index = int(lb.curselection()[0])
    album_name = lb.get(index),

    # get the artist ID from the database row
    album_id = conn.execute('SELECT _albums._id FROM albums WHERE albums.name=?', album_name).fetchone()  # noqa
    alist = []
    for x in conn.execute('SELECT songs.title FROM songs WHERE songs.album=? ORDER BY songs.track', album_id):  # noqa
        alist.append(x[0])
    songLV.set(tuple(alist))

if __name__=='__main__':
    conn = sqlite3.connect('music.sqlite')
    mainWindow = tkinter.Tk()
    mainWindow.title('Music DB Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=1)    # spacer column on right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ===== labels =====
    tkinter.Label(mainWindow, text="Artists").grid(row=0, column=0)
    tkinter.Label(mainWindow, text="Albums").grid(row=0, column=1)
    tkinter.Label(mainWindow, text="Songs").grid(row=0, column=2)

    # ===== Artists Listbox =====
    artistList = DataListBox(mainWindow, conn, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.config(border=2, relief='sunken')

    artistList.requery()


    # ===== Albums Listbox =====
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))  # noqa
    albumList.requery(12)
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    albumList.bind('<<ListboxSelect>>', get_songs)

    # ===== Songs Listbox =====
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))
    songList.requery()
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    # ===== Main loop =====
    testList = range(0, 100)
    albumLV.set(tuple(testList))
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()
