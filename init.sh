sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# sudo gunicorn -c /home/box/web/etc/gunicorn.conf hello:wsgi_appilication
# sudo gunicorn -c /home/box/web/etc/gunicorn_ask.conf ask.wsgi:application

# sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_conf.py
sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask:wsgi_application

#sudo /etc/init.d/gunicorn restart
