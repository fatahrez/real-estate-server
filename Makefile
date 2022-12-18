serve:
	python manage.py runserver
makemigrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
shell:
	python manage.py shell
superuser:
	python manage.py createsuperuser
collectstatic:
	python manage.py collectstatic
initialdata:
	python manage.py loaddata initial_data
set_env_vars:
	@[ -f .env ] && source .env