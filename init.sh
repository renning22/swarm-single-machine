#!/usr/bin/env bash
set -e
set -x

# replace swap ethereum blockchain endpoint
sed -i "s/swap-endpoint-01/$1/" .env

./prepare.sh
./up.sh