"""Learning how to quote in csv files."""

import csv

CSV_FILENAME = 'cereal_grains.csv'

with open(CSV_FILENAME, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
