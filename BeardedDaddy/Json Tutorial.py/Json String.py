import json

json_string = '''
    {
        "students": [
            {
                "ID": 1,
                "Name": "Grevy",
                "Age": 49,
                "Full-Time": true
            },
            {
                "ID": 2,
                "Name": "Mia",
                "Age": 12,
                "Full-Time": false
            }
        ]
    }
'''

data = json.loads(json_string)
print(data['students'][0])
print(data['students'][1])