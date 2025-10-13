from collections import Counter
import json

event_counter = Counter() 
success_counter = Counter()
failure_counter = Counter()
ip_counter = Counter()
username_counter = Counter() 

with open('cowrie.json', 'r') as file:
    for line in file:
        try:
            json_data = json.loads(line)
            event_id = json_data.get('eventid', 'unknown')
            event_counter[event_id] += 1

        except json.JSONDecodeError:
            continue

print("----- Event Counter -----")
for event, count in event_counter.most_common():
    print(f"{event}: {count}")

