""" This module uses the sqlite3 module to interact with a SQLite database.
"""

import sqlite3
import tkinter


# ===== classes =====
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

        self.linked_box = None
        self.link_field = None

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id" + " FROM " + self.table  # noqa
        if sort_order:
            self.sql_sort = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_sort = " ORDER BY " + self.field

    def clear(self):
        """clear class, is used to clear the listbox.
        """
        self.delete(0, tkinter.END)

    def link(self, widget, link_field):
        """link class, is used to link the listbox.
        """
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        """requery class, is used to requery the listbox.
        """
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + "" + self.link_field + "=?" + self.sql_sort  # noqa
            print(sql)   # TODO delete this line
            self.cursor.execute(sql, (link_value,))
        else:
            print(self.sql_select + self.sql_sort)  # TODO delete this line
            self.cursor.execute(self.sql_select + self.sql_sort)

        # clear the listbox contents before re-loading
        self.clear()
        for value in self.cursor:
            self.insert(tkinter.END, value[0])
        if self.linked_box:
            self.linked_box.clear()
            
    def on_select(self, event):
        """on_select class, is used to select the listbox.
        """
        if self.linked_box:
            print(self is event.widget)    # TODO delete this line.
            index = self.curselection()[0]

            # get the artist name from the listbox
            value = self.get(index),

            # get the artist ID from the database row
            link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]  # noqa
            self.linked_box.requery(link_id)


# ===== main =====
if __name__ == '__main__':
    conn = sqlite3.connect('music.sqlite')

    # ===== main window =====
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

    # ===== Scrollbar =====
    scrollbar = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=artistList.yview)  # noqa
    scrollbar.grid(row=1, column=0, sticky='nse', rowspan=2)

# ===== Albums Listbox =====
    albumLV = tkinter.Variable(mainWindow)
    albumLV.set(("Choose an artist",))
    albumList = DataListBox(mainWindow, conn, "albums", "name", sort_order=("name",))  # noqa
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.config(border=2, relief='sunken')

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")

    # albumList.requery()

    # ===== Songs Listbox =====
    songLV = tkinter.Variable(mainWindow)
    songLV.set(("Choose an album",))
    songList = DataListBox(mainWindow, conn, "songs", "title", ("track", "title"))  # noqa
    songList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songList.config(border=2, relief='sunken')

    albumList.link(songList, "album")

    # ===== Main loop =====
    mainWindow.mainloop()
    print("closing database connection")
    conn.close()
