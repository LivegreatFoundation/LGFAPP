#!/bin/bash

# Build the project
set -o errexit  # exit on error
echo "Building the project JDA..."




pip install -r requirements.txt

# python render_migrate.py

python manage.py collectstatic --noinput 

python manage.py makemigrations 
python manage.py migrate --noinput
