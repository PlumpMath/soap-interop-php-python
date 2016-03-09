#
# Build php-cli for either 5.6 or 7 to test soap
#
DOCKERFILE=Dockerfile-php

build:
	docker build -t my-php-app -f $(DOCKERFILE) .
run:
	docker run -it --rm --name my-running-app my-php-app
