""" This line imports the os module.
Yields - We are using the yield keyword to make this generator.
------
    This module in python provides functions for interacting with the operating system.  # noqa
"""
import os
import fnmatch


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
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, f'*.{(extension)}'):
            yield os.path.join(path, file)


for f in find_music('music', 'emp3'):  # The music parameter indicates
    # where to start. The emp3 indicates the file extention to search for.
    print(f)
