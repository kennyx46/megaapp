# Welcome to Megaapp

## Requirements

1. python v3.6
2. postgreSQL

## Start instructions

1. create virtualenv, e.g. `python -m venv megaapp_env`
2. activate virtualenv, e.g. `source ./megaapp_env/bin/activate`
3. install dependencies, `pip install requirements.txt`
4. check the db connection parameters in `megaapp/.env` file, update if necessary. For sqlite: uncomment the sqlite lines in `settings.py` and comment postgres ones
4. migrate db schema `python manage.py migrate`
5. load initial data `python manage.py loaddata initial.json`
6. boot the server `python manage.py runserver`