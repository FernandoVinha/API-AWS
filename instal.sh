apt update
apt upgrade
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt install -y nodejs build-essential
sudo npm install strapi@alpha -g
sudo strapi new nome_do_projeto