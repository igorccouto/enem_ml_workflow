SHELL=/bin/bash

up:
	chmod -R 777 docker
	docker-compose up
	docker ps

up_d:
	chmod -R 777 docker
	docker-compose up -d
	docker ps

stop:
	docker-compose stop

down:
	docker-compose down --volumes
	docker ps

restart:
	docker-compose restart
