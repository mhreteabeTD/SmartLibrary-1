#!/bin/bash

# Apply Django migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# Start your Django project
echo "Starting Django..."
exec "$@"
