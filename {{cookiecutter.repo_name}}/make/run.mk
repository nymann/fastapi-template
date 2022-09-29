run:
	uvicorn ${COMPONENT}.asgi:api --reload --port 5111 --host 0.0.0.0

.PHONY: run
