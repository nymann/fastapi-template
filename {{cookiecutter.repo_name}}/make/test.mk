ensure-test-dependencies:
	command -v pytest 2>/dev/null || make install-tests

test: ${VERSION} ensure-test-dependencies
	pytest tests/unit_tests
