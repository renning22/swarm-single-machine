export PUBLIC_IP=$(curl -s -4 icanhazip.com)
echo "PUBLIC_IP=$PUBLIC_IP"

export BEE_NAT_ADDR=${PUBLIC_IP}:1634
echo "BEE_NAT_ADDR=$BEE_NAT_ADDR"

sudo --preserve-env docker-compose up -d