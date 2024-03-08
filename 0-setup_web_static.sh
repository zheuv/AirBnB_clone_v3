#!/usr/bin/env bash
# acomplex script that does and does and does
trap 'exit 0' ERR

if ! dpkg -s nginx &> /dev/null; then
        sudo apt-get update
        sudo apt-get install nginx -y
fi

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir -p "/data/web_static/shared"

echo "<html>
  <head>
  </head>
  <body>
    Hey u
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html &> /dev/null

rm -rf /data/web_static/current
# Create a new symbolic link
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

# Find the line number of the closing curly brace of the server block
config="/etc/nginx/sites-available/default"
# Use sed to insert the content of $hbnb_static before the closing curly brace
sudo sed -i '/^}/i \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}' $config

sudo service nginx restart
