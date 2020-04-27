#!/bin/bash
service apache2 stop
cp /home/ubuntu/www/shujaaz-comic/apache/default.conf /etc/apache2/sites-available/000-default.conf
service apache2 reload
service apache2 start
