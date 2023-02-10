release: python manage.py migrate && python manage.py collectstatic
web: gunicorn task_manager.wsgi