#!/bin/bash

virtualenv venv
. venv/bin/activate

venv/bin/pip install -r requirements.txt

python createdb.py
python insertintotables.py