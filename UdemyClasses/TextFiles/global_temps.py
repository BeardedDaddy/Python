"""Working on practical application - parsing json data. """

import json
import urllib.request

JSON_DATA_SOURCE = 'https://www.ncdc.noaa.gov/cag/global/time-series'

# with open(JSON_DATA_SOURCE, encoding='utf-8') as data:
with urllib.request.urlopen(JSON_DATA_SOURCE) as json_stream:
    data = json_stream.read().decode('utf-8')
    anomalies = json.loads(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

print(anomalies['citation'])
