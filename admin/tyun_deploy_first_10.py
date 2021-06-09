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
]

for i, host in enumerate(hosts):
    print(f'==== {i:02}/{len(hosts):02} : {host} ====')
    conn = Connection(f'ubuntu@{host}')
    conn.run('hostname')
    try:
        conn.run('git clone https://github.com/renning22/swarm-single-machine.git && cd swarm-single-machine && ./init.sh')
    except UnexpectedExit:
        print('Skip...')
