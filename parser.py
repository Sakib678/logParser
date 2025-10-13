from collections import Counter
import json
import requests
import time

event_counter = Counter() 
success_counter = Counter()
failure_counter = Counter()
ip_counter = Counter()
username_counter = Counter()
port_counter = Counter() 

with open('API_KEY.txt', 'r') as f:
    API_KEY = f.read()


def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    querystring = {'ipAddress': ip,}
    headers = {'Key': API_KEY.strip(), 'Accept': 'application/json'}

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        score = data['data']['abuseConfidenceScore']
        return score
    else:
        return None


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

            dst_port = json_data.get('dst_port')
            if dst_port:
                port_counter[dst_port] += 1

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

print("\n----- Top 10 Ports Attempted -----")
for dst_port, count in port_counter.most_common(10):
    print(f"{dst_port}: {count}")

print("\n----- Checking Top 5 IPs for Malicious Activity -----")
for ip, count in ip_counter.most_common(5):
    score = check_ip(ip)
    if score is None:
        status = "No data"
    elif score == 0:
        status = "Clean"
    elif score < 50:
        status = "Suspicious"
    else:
        status = "Malicious"

    print(f"{ip}: {score} ({status})")
    time.sleep(1)

