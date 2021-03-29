#!/bin/bash

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# Gunicorn
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask_q
sudo ln -sf /home/box/web/etc/ask_conf.conf /etc/gunicorn.d/ask_
sudo gunicorn -c /etc/gunicorn.d/ask_conf.conf ask.wsgi:application
sudo /etc/init.d/gunicorn restart

# run MySQL & create db
sudo /etc/init.d/mysql restart
cd web/ask
mysql -uroot -e "CREATE DATABASE `stepic_web_db`
                DEFAULT CHARACTER SET utf8
                DEFAULT COLLATE utf8_general_ci;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web_db.* TO 'a_user'@'localhost'
                WITH GRANT OPTION;"
mysql -uroot -e "FLUSH PRIVILEGES;"
sudo python3 manage.py makemigrations qa
sudo python3 manage.py migrate qa

sudo /etc/init.d/nginx restart
sudo /etc/init.d/gunicorn restart

