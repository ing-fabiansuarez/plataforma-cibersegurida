#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Create superuser automatically during deployment
python scripts/create_superuser_deploy.py

# Check Django deployment
python manage.py check --deploy
