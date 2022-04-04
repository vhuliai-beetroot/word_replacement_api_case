.PHONY: install local_run docker_build docker_run generate_token test help

IMAGE_NAME?=wr_app
WR_JWK4JWT?=not-a-sceret

install: ## install python dependencies
	install:  ## Install poetry
	@echo "Create poetry virtual environment"
	poetry shell
	@echo "Install required dependencies for the project"
	poetry install

local_run:  ## run application on local machine
	python app

docker_build: ## Build docker image
	docker build -t $(IMAGE_NAME) .

docker_run:  ## run application on local machine via docker
	docker run -p 80:8000 -e WR_JWK4JWT=$(WR_JWK4JWT) $(IMAGE_NAME)

generate_token:  ## generate API token
	python cli.py issue-token

test:  ## run tests
	pytest -vs

help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)