import json

with open('cowrie.json', 'r') as file:
    for line in file:
        try:
            json_data = json.loads(line)
            print(json_data['eventid'])
        except json.JSONDecodeError:
            pass

