#!/usr/bin/env bash
python3 manage.py makemigrations user
python3 manage.py migrate user
python3 manage.py makemigrations comic
python3 manage.py migrate comic
python3 manage.py loaddata shujaaz/apps/user/fixtures/user
python3 manage.py loaddata shujaaz/apps/comic/fixtures/comic

