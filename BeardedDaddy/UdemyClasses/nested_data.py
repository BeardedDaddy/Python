albums = [
    # Index 0
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    # Index 1
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    # Index 2
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    # Index 3
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# Album is index 0
# 
for name, artist, year, songs in albums:
    # Index (Second layer) album [], artist [], year [], songs with track_number in album []
    print("Album: {}, Artist: {}, Year: {}, Songs: {}"
          # Index (third layer) of the Album: album [0] artist [1] year [2] song [3]
          .format(name, artist, year, songs))

print()

album = albums[3] # The one album in the list of albums. With index 3 being "More Mayhem".
# print(album)

songs = album[3] # The list of songs in that previously scripted album. Example: (3, "Mayhem")
# print(songs)

song = songs[2] # The song title only in the list of songs. Index 2 shows (3 [], "Mayhew []")
# print(song)
# print(song[1])

mayhem = albums[3][3][2][1] # Indexes explained: [3] album number 3. [3] track number 3. 
# print(mayhem)

# print(albums[3])
# print(albums[3][3])
print(albums[3][3][2][1])
# In this print statement the first index is calling the album at index [3].
# The second index is calling the list of songs [3]. 
# The third index is calling the song in the list of songs [2].
# The fourth index is calling the song track in the list of songs [1].
# (Example: Album name: More Mayhem [0], Artist: Imelda May [1], Year: 2011 [2], 
# Songs: the List of songs in the album [3], More Mayhem [0], Imelda May [1], 2011 [2], (1,Pulling the Rug), (2, Psycho), (3, Mayhem), (4, Kentish Town Waltz) [3]
# Song: the track from the List [2], 3 [0], Mayhem [1].
# 
# The albums [list] contains 5 tuples -> (each list of songs inside parenthesis
# Inside the (tuples) contains the three items that are separated by commas.
