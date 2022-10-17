"""learning about the zip function. """

import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
# This line creates a column heading in the first row.
keys = ['album', 'artist', 'year']
# The zip function zips together two iterables the tuple from the albums variable and the list from the keys variable and creates a set of tuples.
FILENAME = 'albums.csv'
with open(FILENAME, 'w', encoding='utf-8-sig', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=keys)
    # This line is used to write the column headings to the csv file.
    writer.writeheader()
    for row in albums:
        # This zip functin will combine the header with the items in the list to create a tuple.This function here also creates a zip object created by the zip function.
        zip_object = zip(keys, row)
        # print(zip_object)
        # for thing in zip(keys, row): # This line of code loops thru the zip objects creating a tuple.
        #     print("\t", thing)
        albums_dict = dict(zip_object)
        print(albums_dict)  # This line of code creates a dictionary.
        writer.writerow(albums_dict)  # This line writes each row to the file.
