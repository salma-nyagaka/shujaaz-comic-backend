#!/bin/bash
cd /home/ubuntu/www/shujaaz-comic/
source /home/ubuntu/www/shujaaz-comic/venv/bin/activate
service postgresql start
-u postgres createuser postgres with password 'shujaaz'
-u postgres createdb -O postgres shujaaz
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py makemigrations
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py migrate
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/user/fixtures/user
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/comic/fixtures/comic
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/comic/fixtures/characters
DJANGO_SETTINGS_MODULE=shujaaz.settings SECRET_KEY="mi+xv3xefdu@3bt_&lxhhys-9b#(vkhu*_iot-+5&5h2p%+in9" PSQL_DB_NAME=shujaaz PSQL_DB_USER=postgres PSQL_DB_PASSWD="shujaaz" PSQL_HOST=localhost PSQL_PORT=5432 DATABASE_URL=postgres://shujaaz:''@localhost:5432/shujaaz ./manage.py loaddata /home/ubuntu/www/shujaaz-comic/shujaaz/apps/stories/fixtures/stories
