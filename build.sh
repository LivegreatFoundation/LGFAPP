#!/bin/bash

# Build the project
set -o errexit  # exit on error
echo "Building the project JDA..."




pip install -r requirements.txt

#
python manage.py makemigrations
python manage.py migrate --fake-initial
