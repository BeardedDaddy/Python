"""learning the csv DictReader."""

import csv

CEREAL_FILENAME = 'cereal_grains.csv'

with open(CEREAL_FILENAME, encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)
    for row in reader:
        print(row)
