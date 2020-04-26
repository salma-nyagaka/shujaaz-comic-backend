#!/usr/bin/env bash
yum install -y python-psycopg2 postgresql libncurses5-dev libffi libffi-devel libxml2-devel libxslt-devel libxslt1-dev
yum install -y postgresql-libs postgresql-devel python-lxml python-devel gcc patch python-setuptools
yum install -y gcc-c++ flex epel-release nginx1.12 supervisor
amazon-linux-extras install  nginx1.12
yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs
