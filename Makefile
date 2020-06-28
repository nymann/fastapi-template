TAG:= $(shell git describe --always --dirty)

migrate: install
	@alembic revision -m "${msg}"

upgrade: install
	@alembic upgrade head

run: upgrade
	@uvicorn fastapi_template.asgi:app --reload
build:
	@python setup.py build

install: clean
	@python setup.py install

test: install
	@python setup.py test

lint: install
	@pip install pylint
	@pip install yapf
	@pylint --rcfile=setup.cfg -r n src/ > pylint.txt
	@yapf -dpr src tests migrations

version:
	@echo $(TAG)

.PHONY: clean lint test build install run

clean:
	@rm -rf  __pycache__/ src/fastapi_template.egg-info/ .eggs/ .coverage htmlcov/ dist/ build/ coverage.xml pylint.txt
