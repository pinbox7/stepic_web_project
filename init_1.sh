#!/bin/bash

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# run MySQL & create db
sudo /etc/init.d/mysql restart
# sudo service mysql restart
mysql -uroot -e "DROP DATABASE IF EXISTS `swebdb`;"
mysql -uroot -e "CREATE DATABASE swebdb DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci;"
mysql -uroot -e "CREATE USER 'auser'@'localhost' IDENTIFIED BY '12345678';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON swebdb.* TO 'auser'@'localhost' WITH GRANT OPTION;"
mysql -uroot -e "FLUSH PRIVILEGES;"

#migrate
cd /web/ask
sudo python3 manage.py migrate
sudo /etc/init.d/nginx restart

# Gunicorn
gunicorn -b 0.0.0.0:8000 ask.wsgi:application&

#sudo ln -sf /home/box/web/etc/gunicorn.py /etc/gunicorn.d/ask_q
#sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_
#sudo gunicorn -c /etc/gunicorn.d/ask_conf.conf ask.wsgi:application
#sudo /etc/init.d/gunicorn restart


