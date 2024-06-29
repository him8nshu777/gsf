#!/bin/bash

# Install Python dependencies
python -m pip install -r requirements.txt
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Additional build tasks as needed
