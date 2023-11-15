# This is the Udemy lesson 378

1. Select the titles of all the songs on the album "Forbidden" [X] Done
sqlite> SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY track;

2. Repeat the previous query but this time display the songs in track order. You may want to include the track number in the output to verify that it worked ok [X] Done
sqlite> SELECT songs.title, songs.track FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = "Forbidden" ORDER BY track;

3. Display all songs for the band "Deep Purple" [X]
sqlite> SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id INNER JOIN artists ON albums.artist = artists._id WHERE artists.name = "Deep Purple";

4. Rename the band "Mehitabel" to "One Kitten". Note that this is an exception to the advice to always fully qualify your column names. SET artists.name won't work, you just need to specify name. [X]
sqlite> UPDATE artists SET name = 'One Kitten' WHERE artists.name = "Mehitabel";

5. Check that the record was correctly renamed. [X]
sqlite> SELECT * FROM artists WHERE artists.name = "One Kitten";
_id|name
3|One Kitten

6. Select the titles of all the songs by Aerosmith in alphabetical order. Include only the title in the output. [X]
sqlite> SELECT title FROM artist_list WHERE artis = "Aerosmith" ORDER BY title;

7. Replace the column that you used in the previous answer with count(title) to get just a count of the number songs. [X]
sqlite> SELECT count(title) FROM artist_list WHERE artists = "Aerosmith" ORDER BY title;

8. Search the internet to find out how to get a list of the songs from step 6 without any duplicates. [ ]

9. Search the internet again to find out how to get a count of the songs without duplicates. Hint: It uses the same keyword as step 8 but the syntax may not be obvious. [ ]

10. Repeat the previous query to find the number of artists (which, obviously, should be one) and the number of albums. [ ]


CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);

SELECT songs.title FROM songs WHERE album = "%FORBIDDEN%";

