# List all the songs so that the songs from the same ablum appear together in track order

SELECT * FROM album, songs ORDER BY track;

## Use the select clause to link the songs and albums

Example: SELECT songs.track, songs.title, ablums.name FROM songs JOIN albums ON songs.album = albums._id;

### First thing to do is specifiy what table that the columns are in, track and title are in the songs table, now names comes from the albums table so we specified that as albums.name

### Also what you could write is

SELECT track, title, name FROM songs JOIN albums ON songs.album = albums._id;

### Note that the part where is has songs.album or albums.name or songs.title or songs.track

### what that is the name of the table plus the dot with data name after the dot

CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);