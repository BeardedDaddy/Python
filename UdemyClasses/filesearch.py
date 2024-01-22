""" This line imports the os module.
Yields - We are using the yield keyword to make this generator.
------
    This module in python provides functions for interacting with the operating system.  # noqa
"""
import os
import fnmatch


def find_albums(root, artist_name):
    """ This function creates a function called find_albums to locate
    the albums and artist in the file directory.
    """

    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):

        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):  # noqa
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):  # noqa
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


def find_songs(albums):
    """find_songs is a function to search for albums
    in the file directory.

    Parameters
    ----------
    albums
        Albums is the column name in this table.

    Yields
    ------
        The yield keyword is used here to iterate thru
        each time the function is called.
    """
    for album in albums:
        for song in os.listdir(album[0]): # We want the path, not the name of the album.  # noqa
            yield song


album_list = find_albums("music", "black*")
song_list = find_songs(album_list)

for s in song_list:
    print(s)
