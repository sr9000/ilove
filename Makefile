# Self-documented Makefile

.DEFAULT_GOAL := help

.PHONY: help init-venv init-poetry install-requirements run web clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

venv:  ## Create a virtual environment
	python3 -m venv venv

poetry:  ## Set up Poetry environment
	poetry install

requirements:  ## Install requirements.txt using pip
	pip install -r requirements.txt

run:  ## Run desktop application
	flet run

web:  ## Run the application in browser
	flet run --web
