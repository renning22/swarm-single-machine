import time

from fabric import Connection

hosts = [
    "118.193.45.223",
    "128.1.135.208",
    "103.14.34.147",
    "23.91.97.32",
    "152.32.210.117",
    "23.91.98.101",
    "152.32.189.174",
    "36.255.220.243",
    "152.32.192.130",
    "101.36.117.63",
    "101.36.120.12",
    "101.36.122.83",
    "152.32.215.147",
    "152.32.251.236"
]

while True:
    for i, host in enumerate(hosts):
        print(f'==== {i:02}/{len(hosts):02} : {host} ====')
        conn = Connection(f'ubuntu@{host}')
        conn.run('hostname')
        result = conn.run(
            "curl -s http://localhost:1635/peers | jq '.peers | length'", hide=True)
        print(f'peers = {result.stdout.strip()}')
        if not result.stdout.strip():
            print('Restarting...')
            conn.run('cd swarm-single-machine && ./restart.sh')

    time.sleep(60)
