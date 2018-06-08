install:
	python3 -m venv venv
	virtualenv venv

init:
	pip3 install -r requirements.txt

clean-pyc:
	@echo "Limpando o projeto"
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '__pycache__' -exec rm -fr {} +

run:
	@echo "Executando o projeto"
	python3 manage.py runserver

.PHONY: init run clean-pyc
	