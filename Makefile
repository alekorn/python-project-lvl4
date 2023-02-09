.PHONY: lint run
run:
		poetry run python manage.py runserver 9000
lint:
		poetry run flake8 task_manager
test:
		poetry run python manage.py test polls
shell:
		poetry run python manage.py shell