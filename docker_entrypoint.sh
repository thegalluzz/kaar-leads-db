#!/bin/sh

echo "Waiting for db..."

while ! nc -z db 3306; do
    sleep 0.1
done

echo "MariaDB started"

python /usr/src/app/manage.py migrate
python /usr/src/app/manage.py collectstatic --noinput

exec "$@"