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

            if event_id == 'cowrie.login.success':
                success_counter[event_id] += 1
            elif event_id == 'cowrie.login.failed':
                failure_counter[event_id] += 1

            src_ip = json_data.get('src_ip')
            if src_ip:
                ip_counter[src_ip] += 1

            username = json_data.get('username')
            if username:
                username_counter[username] += 1

        except json.JSONDecodeError:
            continue

print("----- Event Counter -----")
for event, count in event_counter.most_common():
    print(f"{event}: {count}")

print("\n----- Successful Logins -----")
for event, count in success_counter.most_common():
    print(f"{event}: {count}")

print("\n----- Failed Logins -----")
for event, count in failure_counter.most_common():
    print(f"{event}: {count}")

print("\n----- Top 10 Source IPs -----")
for ip, count in ip_counter.most_common(10):
    print(f"{ip}: {count}")

print("\n----- Top 10 Usernames Attempted -----")
for user, count in username_counter.most_common(10):
    print(f"{user}: {count}")


