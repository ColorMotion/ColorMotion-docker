help:
	@cat Makefile

DATA?="${HOME}/Data"
GPU?=1
DOCKER_FILE=Dockerfile
DOCKER=GPU=$(GPU) nvidia-docker
BACKEND=tensorflow
KERAS_VERSION?=2.1.6
TAG?=tiagoshibata/keras:latest
TEST=tests/
SRC?=$(shell dirname `pwd`)

build:
	docker build -t $(TAG) --build-arg keras_version=$(KERAS_VERSION) -f $(DOCKER_FILE) .

bash: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) $(TAG) bash

ipython: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) $(TAG) ipython

notebook: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data --net=host --env KERAS_BACKEND=$(BACKEND) $(TAG)

test: build
	$(DOCKER) run -it -v $(SRC):/src/workspace -v $(DATA):/data --env KERAS_BACKEND=$(BACKEND) $(TAG) py.test $(TEST)
