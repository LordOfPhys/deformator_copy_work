#!/usr/bin/env bash
python manage.py collectstatic --noinput
python manage.py migrate --noinput
uwsgi --ini /etc/uwsgi.ini --uid root --gid root
