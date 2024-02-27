#!/bin/sh

echo 'Running collectstatic...'
python 'yes' | manage.py collectstatic --settings=config.settings.production
echo 'Applying migrations...'
python manage.py migrate --settings=config.settings.production
echo 'Running server...'
gunicorn --workers 4 --env DJANGO_SETTINGS_MODULE=config.settings.production config.wsgi:application --bind 0.0.0.0:8000

