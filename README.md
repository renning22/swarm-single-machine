* Install Docker Engine
    * https://docs.docker.com/engine/install/ubuntu/
* Install Docker Compose
    * https://docs.docker.com/compose/install/

mkdir -p /data/clef
sudo chown -R nobody:nogroup /data/clef

mkdir -p /data/bee
sudo chown -R 999:999 /data/bee

sudo docker-compose up -d
sudo docker-compose logs -f clef-1
sudo docker-compose logs -f bee-1
sudo docker-compose down