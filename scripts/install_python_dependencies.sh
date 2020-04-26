#!/usr/bin/env bash
chown ec2-user:ec2-user /home/ec2-user/www
yum install python3 python3-devel python3-libs python3-tools
pip3 install virtualenv
virtualenv /home/ec2-user/www/project-venv
chown ec2-user:ec2-user /home/ec2-user/www/project-venv
chown ec2-user:ec2-user /home/ec2-user/www/project-venv/*
source /home/ec2-user/www/project-venv/bin/activate
pip3 install -r /home/ec2-user/www/shujaaz-comic/requirements.txt
