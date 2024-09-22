export APP := datapains
export TAG := 0.0.1
export DOCKERFILE_PATH := tools/docker/example-app
export DOCKER_BUILD := build

.PHONY: build-example-app-image
build-example-app-image:
	docker $(DOCKER_BUILD) -t $(APP)/prometheus-example-app:$(TAG) -f $(DOCKERFILE_PATH)/$(COMPONENT)/Dockerfile tools/docker/example-app
