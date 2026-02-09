#!/bin/bash
set -e

export $(grep -v '^#' .env | xargs)

echo "🔄 Ожидание PostgreSQL..."
while ! nc -z db 5432; do
  sleep 0.5
done
echo "✅ PostgreSQL доступен"

echo "🔄 Ожидание PgBouncer..."
while ! nc -z pgbouncer ${PGBOUNCER_PORT}; do
  sleep 0.5
done
echo "✅ PgBouncer доступен"

echo "📦 Применение миграций..."
python manage.py migrate --noinput

#echo "🧹 Удаление sourceMappingURL из bootstrap.min.css..."
#find . -name "bootstrap.min.css" -exec sed -i '/sourceMappingURL/d' {} \;

echo "🧼 Сборка статики..."
python manage.py collectstatic --noinput

echo "🚀 Запуск Gunicorn..."
exec gunicorn src.wsgi:application \
    --bind 0.0.0.0:$ADMIN_PORT \
    --workers=4 \
    --threads=2 \
    --worker-class=gthread \
    --access-logfile - \
    --error-logfile - \
    --capture-output \
    --log-level debug


#exec gunicorn src.asgi:application \
#    --worker-class=uvicorn.workers.UvicornWorker \
#    --bind 0.0.0.0:$WEB_PORT