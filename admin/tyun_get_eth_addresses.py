# Must be run from Jump Server.
#
#  ssh root@148.153.205.10 -i /home/ningr/tyun/id_rsa
#  (pip install fabric)
#
#  clone https://github.com/renning22/swarm-single-machine.git
#  cd swarm-single-machine
#
#  python3 tyun_get_eth_addresses.py

from fabric import Connection
from invoke import UnexpectedExit

hosts = [
    'BEE-xh001',
    'BEE-xh002',
    'BEE-xh003',
    'BEE-xh004',
    'BEE-xh005',
    'BEE-xh006',
    'BEE-xh007',
    'BEE-xh008',
    'BEE-xh009',
    'BEE-xh010',
]

for i, host in enumerate(hosts):
    print(f'==== {i:02}/{len(hosts):02} : {host} ====')
    conn = Connection(host)
    conn.run('cd swarm-single-machine && ./addresses.sh')
    print()