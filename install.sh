#!/bin/bash

virtualenv venv
. venv/bin/activate
git pull origin master

venv/bin/pip install -r requirements.txt

python createdb.py