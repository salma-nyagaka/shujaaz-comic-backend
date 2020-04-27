#!/bin/bash
chown ubuntu:ubuntu /home/ubuntu/www
apt-get install python3-pip libapache2-mod-wsgi-py3
pip3 install virtualenv
virtualenv /home/ubuntu/www/shujaaz-comic/venv
chown ubuntu:ubuntu /home/ubuntu/www/shujaaz-comic/venv
chown ubuntu:ubuntu /home/ubuntu/www/shujaaz-comic/venv/*
source /home/ubuntu/www/shujaaz-comic/venv/bin/activate
pip3 install -r /home/ubuntu/www/shujaaz-comic/requirements.txt
