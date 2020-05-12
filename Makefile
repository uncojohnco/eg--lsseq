.PHONY: help tests

help: ## This help
	@echo "Makefile for lss:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


install-dev: ## install pip requirements for `dev` env
	pip-sync requirements/dev.txt

lint: ## run flake8 linter
	tox -e flake8


tests: ## run tests
	tox


tests-doctest-modules: ## run tests - docmodules
	tox -e doctest-modules


tests-all: tests ## run tests - all
	$(MAKE) tests
	$(MAKE) tests-docmodules


requirements-clean-all: ## clean compiled `requirements` and recompile
	$(MAKE) -C requirements clean all
