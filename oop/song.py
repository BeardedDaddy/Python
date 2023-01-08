class Song:
    """ Class to represent a song

    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing  the songs creator.
        duration (int): The duration of the song in seconds. May be zero
    """

def __init__(self, title, artist, duration=0):
    """Song init method
    
    Args:
        title (str): Initialises the 'title' attribute
        artist (Artist): At Artist object representing the song's creator.
        duratin (Optional[int]): Initial value for the 'duration' attribute.
            Will default to zero if  not specified.
    """
    self.title = title
    self.artist = artist
    self.duration = duration
