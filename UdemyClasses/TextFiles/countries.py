"""In this code block we are parsing data in a text file."""


INPUT_FILENAME = 'country_info.txt'
countries = {}
# This is an empty dictionary.
with open(INPUT_FILENAME, encoding='utf-8') as country_file:
    for row in country_file:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
       # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': country,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency,
        }
       # print(country_dict)
        countries[country.casefold()] = country_dict

# print(countries)

while True:
    chosen_country = input('Please enter the name of a country: ')
    country_key = chosen_country.casefold()
    if country_key in countries:
        country_data = countries[country_key]
        print(country_data)
        print(country_data['capital'])
        print(f"The capital of {chosen_country} is {country_data['capital']}")
    elif chosen_country != countries:
        print('This is not a country in the list.')
    elif chosen_country == 'quit':
    #     print(input('Do you want to stop? '))
    # else:
        break
