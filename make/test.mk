test: test-${TARGET}

test-docker: ${VERSION} requirements.install
	${SCRIPTS_DIR}/docker_test.sh

test-local: ${VERSION} requirements.install
	@pip install -e .
	@python setup.py test

test-ci: test-local
	@docker-compose exec -T fastapi_template make TARGET=local test

test-production:
