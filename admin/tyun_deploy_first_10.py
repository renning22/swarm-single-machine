# Must be run from Jump Server.
#
#  ssh root@148.153.205.10 -i /home/ningr/tyun/id_rsa
#  clone https://github.com/renning22/swarm-single-machine.git
#  cd swarm-single-machine
#  python3 tyun_deploy_first_10.py

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
    conn.run('hostname')
    try:
        conn.run('git clone https://github.com/renning22/swarm-single-machine.git && cd swarm-single-machine && ./init.sh')
    except UnexpectedExit:
        print('Skip...')
