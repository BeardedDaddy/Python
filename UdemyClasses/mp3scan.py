""" This line imports the os module.
Yields - We are using the yield keyword to make this generator.
------
    This module in python provides functions for interacting with the operating system.  # noqa
"""
import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    """find_music is a function with two parameters,
    one that has a start parameter and the second to for the extention.

    Parameters
    ----------
    start
       This parameter indicates where we start the search.
    extension
        This parameter indicates the files with a certain
        file extention.

    Yields
    ------
        The yield keyword iterates over the generator
        returned by the find_music function.
    """
    for path, _, files in os.walk(start):
        for file in fnmatch.filter(files, f'*.{extension}'):
            absolute_path = os.path.abspath(path)       # Creating absolute path  # noqa
            yield os.path.join(absolute_path, file)      # use it in yield values  # noqa


my_music_files = find_music("/Users/grevy/OneDrive/Music/", "mp3")

error_list = []
for f in my_music_files:  # The music parameter indicates
    # where to start. The emp3 indicates the file extention to search for.
    try:
        id3r = id3reader.Reader(f)
        print(f"Artist: {id3r.get_value('performer')}, "
              f"Album: {id3r.get_value('album')}, "
              f"Track: {id3r.get_value('track')}, "
              f"Song: {id3r.get_value('title')}")

    except:
        error_list.append(f)


for error_file in error_list:
    print(error_file)
