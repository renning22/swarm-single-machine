#!/usr/bin/env bash

git pull
sudo docker-compose pull

./down.sh
./up.sh