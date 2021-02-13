#!/bin/sh

set -e

# collect static files to rool vol
python manage.py collectstatic --noinput

ls -l

# run the application - tcp at port 8000
# uwsgi --socket :8000 --master --enable-threads --module app.wsgi
# cd app

gunicorn --bind :8000 fullThrottleTest.wsgi:application