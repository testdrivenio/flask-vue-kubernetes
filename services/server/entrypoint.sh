#!/bin/sh

# echo "Waiting for postgres..."

while ! nc -z postgres 5432; do
  sleep 0.1
done

# echo "PostgreSQL started"

python manage.py recreate_db
python manage.py seed_db
python manage.py run --host 0.0.0.0
# gunicorn -b 0.0.0.0:5000 manage:app
