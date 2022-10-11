"""In this code block we are parsing data in a text file."""

import csv

INPUT_FILENAME = 'country_info.txt'
countries = {}
# This is an empty dictionary.
with open(INPUT_FILENAME, encoding='utf-8', newline='') as country_file:
    dict_reader = csv.DictReader(country_file, delimiter='|')
    for row in dict_reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(f"The capital of {chosen_country} is {country_data['Capital']}")
    elif chosen_country == 'quit':
        break
