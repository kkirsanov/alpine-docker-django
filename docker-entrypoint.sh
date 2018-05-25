#!/bin/sh
# Exit immediately if a command exits with a non-zero status.
# http://stackoverflow.com/questions/19622198/what-does-set-e-mean-in-a-bash-script
set -e

case "$1" in

    web)
        echo "Running App (gunicorn)..."
        python3.6 manage.py migrate --noinput
        python3.6 manage.py collectstatic --noinput
        exec gunicorn app.wsgi -b 0.0.0.0:8000 -w 2 -t 120
    ;;
    celery)
        echo "Running Celery..."
        exec celery worker -A app -Q queue --concurrency=4
    ;;

esac
