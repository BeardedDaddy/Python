"""learning about the sniffer and dialect."""
import csv

INPUT_FILENAME = 'country_info.txt'

with open(INPUT_FILENAME, encoding='utf-8', newline='') as countries_data:
    SAMPLE = ""
    for line in range(3):
        SAMPLE += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(SAMPLE)
    country_dialect.skipinitialspace = True
    countries_data.seek(0)
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace',
              ]
for attribute in attributes:
    print(f'{attribute}: {repr(getattr(country_dialect, attribute))}')
