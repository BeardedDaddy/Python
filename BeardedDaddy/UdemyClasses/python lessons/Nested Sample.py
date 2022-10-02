albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lighting", "Metallica", 1984)
        ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Years: {}".format(name, artist, year))
print()
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Years: {}".format(name, artist, year))


# The albums [list] contains 5 tuples -> (each list of songs inside parentheses)
# Inside the (tuples) contains the three items that are separated by commas.
