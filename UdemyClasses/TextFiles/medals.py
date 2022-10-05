"""Learning how to read a csv file"""
import csv

CSV_FILENAME = 'OlympicMedals_2020.csv'

with open(CSV_FILENAME, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').strip(',')
    print(f'Colomn headers: {headers}')
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
