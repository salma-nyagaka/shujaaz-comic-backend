#!/usr/bin/env bash
cd /home/ec2-user/www/shujaaz-comic/
source /home/ec2-user/www/project-venv/bin/activate
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=shujaaz PSQL_HOST=127.0.0.1 PSQL_PORT=5432 ./manage.py makemigrations
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=shujaaz PSQL_HOST=127.0.0.1 PSQL_PORT=5432 ./manage.py migrate
