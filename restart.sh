#!/usr/bin/env bash
local_swap_endpoint_ip=$(grep "swap-endpoint" .env |cut -d"/" -f3|cut -d":" -f1)

git pull
sudo docker-compose pull

sed -i "s/swap-endpoint-01/$local_swap_endpoint_ip/" .env

./down.sh
./up.sh