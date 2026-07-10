echo="Running daphne server..."
daphne -b 127.0.0.1 -p 8000 live_emergency_coordination_platform.asgi:application