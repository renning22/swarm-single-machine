#!/usr/bin/env bash
#
# Usage:
#   ./init.sh ws://10.7.17.210:8546
set -e
set -x

# add swap ethereum blockchain endpoint
printf "BEE_SWAP_ENDPOINT=$1\n" > .env

./prepare.sh
./up.sh