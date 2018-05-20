BACKEND?=tensorflow
DOCKER=nvidia-docker
TAG?=tiagoshibata/colormotion

build:
	docker build -t $(TAG) .

bash: build
	$(DOCKER) run -ti -v $(PWD)/../volume:/volume --env KERAS_BACKEND=$(BACKEND) $(TAG) bash

# notebook: build
# 	$(DOCKER) run -ti -v $(PWD)/../volume:/volume --net=host --env KERAS_BACKEND=$(BACKEND) $(TAG)
