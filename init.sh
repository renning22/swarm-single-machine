#!/usr/bin/env bash
set -e
set -x

# add swap ethereum blockchain endpoint
printf "BEE_SWAP_ENDPOINT=$1\n" | tee -a .env

./prepare.sh
./up.sh