# Self-documented Makefile

.DEFAULT_GOAL := help

.PHONY: help venv poetry poetry-export pip-freeze requirements run web format

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

venv:  ## Create a virtual environment
	python3 -m venv venv

poetry:  ## Set up Poetry environment
	poetry install

poetry-export: ## Export Poetry dependencies to requirements.txt
	poetry export -f requirements.txt --output requirements.txt --without-hashes

pip-freeze: ## Export pip dependencies to requirements.txt
	pip freeze > requirements.txt

requirements:  ## Install requirements.txt using pip
	pip install -r requirements.txt

run:  ## Run desktop application
	flet run

web:  ## Run the application in browser
	flet run --web --port 8000

format:  ## Run isort then black code formatters on src
	@echo -n "\n#1: "
	isort src

	@echo -n "\n#2: "
	black src
