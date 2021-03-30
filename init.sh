#!/bin/bash

# Nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# Gunicorn
sudo ln -sf /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/ask_q
sudo ln -sf /home/box/web/etc/ask_conf.conf /etc/gunicorn.d/ask_
# sudo gunicorn -c /etc/gunicorn.d/ask_conf.conf ask.wsgi:application
sudo /etc/init.d/gunicorn restart

# run MySQL & create db
sudo /etc/init.d/mysql restart
mysql -uroot -e "create database stepic_web_db"
