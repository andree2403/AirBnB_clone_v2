#!/usr/bin/python3

apt-get -y update
apt-get -y install nginx
ufw allow 'Nginx HTTP'
mkdir data
cd data
mkdir web_static
cd web_static
mkdir releases
mkdir shared
cd releases
mkdir test
cd test
touch index.html
echo 'Hello World!' > /data/web_static/releases/test/index.html
sudo chmod -R 755 /data/
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
