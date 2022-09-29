"""In this code block we are parsing data in a text file."""
INPUT_FILENAME = 'country_info.txt'

with open(INPUT_FILENAME, encoding = 'utf-8') as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        