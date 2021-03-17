#!/bin/bash

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# Gunicorn
# sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_conf.py
sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask.wsgi:application
sudo /etc/init.d/gunicorn restart

# run MySQL & create db
sudo /etc/init.d/mysql restart
mysql -uroot -e "create database stepic_web_db"