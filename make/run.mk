run: run-${TARGET}

run-local:
	@uvicorn ${COMPONENT}.asgi:app --reload --port 9001 --host 0.0.0.0

run-docker: install-docker
	@docker-compose up

run-ci:
	@echo "WRONG USAGE: Don't use run as part of CI."
	exit 2

run-production:
	@echo "WRONG USAGE: Don't run code in production."
	exit 2
