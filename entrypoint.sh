#!/bin/bash
set -e

python manage.py migrate --noinput
python manage.py collectstatic --noinput

echo "Running daphne server..."
exec daphne -b 0.0.0.0 -p 7000 live_emergency_coordination_platform.asgi:application
