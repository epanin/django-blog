start:
	poetry run python manage.py runserver
migrate:
	poetry run python menage.py makemigrations
	poetry run python manage.py migrate
