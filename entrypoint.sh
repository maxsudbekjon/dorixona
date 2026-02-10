#!/bin/bash
set -e

export $(grep -v '^#' .env | xargs)

echo "Waiting PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.5
done
echo "PostgreSQL is enabled"

echo "Process migrating..."
python manage.py migrate --noinput

#echo "🧹 Удаление sourceMappingURL из bootstrap.min.css..."
#find . -name "bootstrap.min.css" -exec sed -i '/sourceMappingURL/d' {} \;

echo "Collecting static..."
python manage.py collectstatic --noinput

echo "Running Gunicorn..."
exec gunicorn config.wsgi:application \
    --bind 0.0.0.0:$WEB_PORT \
    --workers=4 \
    --threads=2 \
    --worker-class=gthread \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    --log-level info


#exec gunicorn src.asgi:application \
#    --worker-class=uvicorn.workers.UvicornWorker \
#    --bind 0.0.0.0:$WEB_PORT