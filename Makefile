migrate: install
	@alembic revision -m "${msg}"

upgrade: install
	@alembic upgrade head

docker-run:
	@docker-compose build
	@docker-compose up -d

docker-logs:
	@docker-compose logs -f

run: upgrade
	@uvicorn fastapi_template.asgi:app --reload
build:
	@python setup.py build

install: clean
	@python setup.py develop

test: install
	@python setup.py test


DB ?= fastapi_template
clean_db: clean
	@psql -U postgres -d ${DB} -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

lint: yapf pylint

pylint:
	@pip install pylint
	@pylint --rcfile=setup.cfg -r n src > pylint.txt
	@cat pylint.txt

yapf:
	@pip install yapf
	@yapf -dpr src tests migrations

watch-cov: test
	@ls | entr firefox htmlcov/index.html

.PHONY: clean lint test build install run docker-run migrate clean_db yapf pylint

clean:
	@rm -rf  __pycache__/ src/fastapi_template.egg-info/ .eggs/ .coverage htmlcov/ dist/ build/ coverage.xml pylint.txt

hooks:
	@pip install pre-commit
	@pre-commit install
