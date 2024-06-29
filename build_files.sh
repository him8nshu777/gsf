#!/bin/bash
# Ensure Python is on the PATH
export PATH="/usr/local/bin:$PATH"

# Install Python dependencies using Python 3
python -m pip install -r requirements.txt
# Install Python dependencies
python -m pip install -r requirements.txt
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Additional build tasks as needed
