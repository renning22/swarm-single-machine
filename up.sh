PUBLIC_IP=$(curl -s icanhazip.com)
echo "PUBLIC_IP=$PUBLIC_IP"

BEE_NAT_ADDR=${PUBLIC_IP}:1634
echo "BEE_NAT_ADDR=$PUBLIC_IP"

sudo --preserve-env docker-compose up -d 