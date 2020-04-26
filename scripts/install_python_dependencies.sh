#!/usr/bin/env bash
chown ec2-user:ec2-user /home/ec2-user/www
virtualenv /home/ec2-user/www/shujaaz-comic-venv
chown ec2-user:ec2-user /home/ec2-user/www/shujaaz-comic-venv
chown ec2-user:ec2-user /home/ec2-user/www/shujaaz-comic-venv/*
source /home/ec2-user/www/shujaaz-comic-venv/bin/activate
pip install -r /home/ec2-user/www/shujaaz-comic/requirements.txt
