.PHONY: help

help: ## This help
	@echo "Makefile for lss:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


install-dev: ## install pip requirements for `dev` env
	pip install -r requirements/dev.txt

lint: ## run flake8 linter
	flake8

test: ## run tests
	pytest $(args)

requirements-clean-all: ## clean compiled `requirements` and recompile
	$(MAKE) -C requirements clean all
