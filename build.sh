#!/usr/bin/env bash

# Install dependencies (Render does this automatically but good for safety)
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
