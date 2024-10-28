.PHONY: build up down migrate test

build:
	docker-compose build

run:
	docker-compose up -d

down:
	docker-compose down

migrate:
	docker-compose run --rm web python manage.py migrate

test:
	docker-compose run --rm web python manage.py test

shell:
	docker-compose run --rm web python manage.py shell

makemigrations:
	docker-compose run --rm web python manage.py makemigrations