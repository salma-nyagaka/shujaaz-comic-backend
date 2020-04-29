#!/bin/bash
export DJANGO_SETTINGS_MODULE=shujaaz.settings 
export SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" 
export PSQL_DB_NAME=shujaaz 
export PSQL_DB_USER=www-data
export PSQL_DB_PASSWD="shujaaz" 
export PSQL_HOST=localhost 
export PSQL_PORT=5432 
export DATABASE_URL=postgres://"www-data":'shujaaz'@localhost:5432/shujaaz 

cd /home/ubuntu/www/shujaaz-comic/
source /home/ubuntu/www/shujaaz-comic/venv/bin/activate
service postgresql start

./manage.py makemigrations
./manage.py migrate
./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/user/fixtures/user
./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/comic/fixtures/comic
./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/comic/fixtures/characters
./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/stories/fixtures/stories
