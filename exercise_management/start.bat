export DJANGO_SETTINGS_MODULE=settings.production
python manage.py makemigrations
python manage.py migrate
uvicorn exercise_management.asgi:application --port 8000 --workers 2
uvicorn exercise_management.asgi:application --port 8001 --workers 2
