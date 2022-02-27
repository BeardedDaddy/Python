albums = [
    # Index 0
    # Inside this index name [0], artist [1], year [2]
    ("Welcome to my Nightmare", "Alice Cooper", 1975
        ,
    [# Inside this index songs [3], index track number [4], index song [5]
        (1), ("Welcome to my Nightmare"),
        (2), ("Devil's Food"),
        (3), ("The Black Widow"),
        (4), ("Some Folks"),
        (5), ("Only Women Bleed"),
    ]
    ),
    # Index 1
    # Inside this index name [0], artist [1], year [2]
    ("Bad Company", "Bad Company", 1974,
     #Inside this index track [3], song [4]
    [
        (1), ("Can't Get Enough"),
        (2), ("Rock Steady"),
        (3), ("Ready for Love"),
        (4), ("Don't Let Me Down"),
        (5), ("Bad Company"),
        (6), ("The Way I Choose"),
        (7), ("Movin' On"),
        (8), ("Seagull"),
    ]
    ),
    # Index 2
        # Inside this index name [0], artist [1], year [2]
    ("Nightflight", "Budgie", 1981,
      [# Inside this index track [3], song [4]
            (1), ("I Turned to Stone"),
            (2), ("Keeping a Rendezvous"),
            (3), ("Reaper of the Glory"),
            (4), ("She Used Me Up"),
        ]
        ),
        # Index 3
        # Inside this index name [0], artist [1], year [2]
    ("More Mayham", "Imelda May", 2011,
     [# Inside this index track [3], song [4]
         (1), ("Pulling the Rug"),
         (2), ("Psycho"),
         (3), ("Mayhem"),
         (4), ("Kentish Town Waltz"),
     ]
     ),
        ]
# for name, artist, year, songs in albums:
#     print("Albums: {}, Artist: {}, Year: {}, Songs: {}".format(name, artist, year, songs))
    
print()

album = albums[2]
# print(album)

songs = album[3]
track = songs[0]
print(track)
    
    # Index 1
    # Inside this index name [0], artist [1], year [2]
    
    # The output from your program should be
    # The Way I Choose (Index album 1)(Index song 5)
    # 1981 (Index album 2) (index year 2)
    # 4 (Index album 1) (Index )
    # (2, 'Keeping a Rendezvous')
    
