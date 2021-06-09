# curl --data '{"method":"eth_blockNumber","params":[],"id":1,"jsonrpc":"2.0"}' -H "Content-Type: application/json" -X POST localhost:8545

sudo docker run --detach \
  -p 8545:8545 \
  -p 8546:8546 \
  -p 30303:30303 \
  -v /data/ethereum:/root/.ethereum \
  ethereum/client-go:stable --syncmode "light" --cache=512 --rpc --rpcaddr "0.0.0.0" --ws --ws.addr "0.0.0.0" --goerli --rpcvhosts=*
