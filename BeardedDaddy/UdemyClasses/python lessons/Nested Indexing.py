albums = [
    # Index 0 Album
    # Inside this index name [0], artist [1], year [2]
    ("Welcome to my Nightmare", "Alice Cooper", 1975
        ,
    [# Inside this index songs [3],
    #  Index the list of songs -there are five List of songs- 
    # The List starts at [0] Welcome to my Nightmare, [1] Devil's Food, [2] The Black Widow, [3] Some Folks, [4] Only Women Bleed
    #  Index [0] the track number, index song [1] the song name
        (1, "Welcome to my Nightmare"),
        (2, "Devil's Food"),
        (3, "The Black Widow"),
        (4, "Some Folks"),
        (5, "Only Women Bleed"),
    ]
    ),
    # Index 1 Album
    # Inside this index name [0], artist [1], year [2]
    ("Bad Company", "Bad Company", 1974,
     
    # Inside this index songs [3],
    #  Index the list of songs -there are five List of songs- 
    # The List starts at [0] Can't Get Enough, [1] Rock Steady, [2] Ready for Love, [3] Don't Let Me Down, [4] Bad Company, [5] The Way I Choose,
    # [6] Movin' On, [7] Seagull
    #  Index [0] the track number, index song [1] the song name

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
    # Index 2 Album
        # Inside this index name [0], artist [1], year [2]
    ("Nightflight", "Budgie", 1981,
     
    # Inside this index songs [3],
    #  Index the list of songs -there are five List of songs- 
    # The List starts at [0] I Turned to Stone, [1] Keeping a Rendezvous, [2] Reaper of the Glory, [3] She Used Me Up.
    #  Index [0] the track number, index song [1] the song name
        [
        (1, "I Turned to Stone"),
        (2, "Keeping a Rendezvous"),
        (3, "Reaper of the Glory"),
        (4, "She Used Me Up"),
        ]
        ),
        # Index 3 Album
        # Inside this index name [0], artist [1], year [2]
    ("More Mayham", "Imelda May", 2011,
     
    # Inside this index songs [3],
    #  Index the list of songs -there are five List of songs- 
    # The List starts at [0] Pulling the Rug, [1] Psycho, [2] Mayhem, [3] Kentish Town Waltz.
    #  Index [0] the track number, index song [1] the song name
    [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
        ]
# print()
# for name, artist, year, songs in albums:
#       print("Album: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))
      
print()

album = albums[1]
print(albums)

print()

songs = albums[3]
print(songs)

print()

song = songs[3]
print(song)
# print(song[1])
    # Index 1
    # Inside this index name [0], artist [1], year [2]
    
# The output from your program should be
    
# The Way I Choose
print(albums[1][3][5][1])
# 1981
print(albums[2][2])    
# 4
print(albums[0][3][3][0])    
# Keeping a Rendezvous
print(albums[2][3][1][1])
