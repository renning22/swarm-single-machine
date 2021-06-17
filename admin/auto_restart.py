import itertools
import time
from datetime import datetime

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
    "152.32.251.236",
    "152.32.190.173",
    "23.91.101.163",
    "118.193.39.223",
    "165.154.3.36",
    "45.249.247.180",
    "152.32.210.173",
]

for epoch in itertools.count(start=1):
    print()
    print(f'epoch = {epoch}, current time = {datetime.now()}')

    for i, host in enumerate(hosts):
        print(f'==== {i:02}/{len(hosts):02} : {host} ====')
        with Connection(f'ubuntu@{host}') as conn:
            conn.run('hostname')
            result = conn.run(
                "curl -s http://localhost:1635/peers | jq '.peers | length'", hide=True)
            print(f'peers = {result.stdout.strip()}')
            if not result.stdout.strip():
                print('Restarting...')
                conn.run('cd swarm-single-machine && ./restart.sh')
            conn.run('curl -s localhost:1635/chequebook/cheque | jq')
            conn.run('cd swarm-single-machine && ./cashout.sh')

    time.sleep(60)
