## Prerequisites

* Install Docker Engine
    * https://docs.docker.com/engine/install/ubuntu/
* Install Docker Compose
    * https://docs.docker.com/compose/install/

## Prepare 

```
git clone https://github.com/renning22/swarm-single-machine.git
cd swarm-single-machine
```

```
mkdir -p /data/clef
sudo chown -R nobody:nogroup /data/clef
mkdir -p /data/bee
sudo chown -R 999:999 /data/bee
```
## Start Node

1. Start docker containers clef-1 + bee-1.
```
./up.sh
```

2. Get addresses
```
./addresses.sh
```
3. Verify ETH address and P2P PUBLIC_IP:1634
4. Fund this ETH address (1 ETH + 1 BZZ)!
5. Verify there are peers
```
./peers
```
## Cashout once a day!
```
./cashout cashout-all
```