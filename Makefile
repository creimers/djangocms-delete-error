DOCKER := $(shell which docker-compose)

all: build

build:
	docker-compose build

runserver: $(DC)
	docker-compose run -p 8000:8000 django python ./manage.py runserver 0.0.0.0:8000

migrate: $(DC)
	docker-compose run django python ./manage.py migrate

superuser: $(DC)
	docker-compose run django python ./manage.py createsuperuser

shell: $(DC)
	docker-compose run django python ./manage.py shell
