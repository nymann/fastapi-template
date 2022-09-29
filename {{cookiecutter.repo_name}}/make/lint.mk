ensure-lint-dependencies:
	command -v black flake8 mypy 2>/dev/null || make install-dev

ensure-fix-dependencies:
	command -v black isort 2>/dev/null || make install-dev


lint: ensure-lint-dependencies $(VERSION)
	@black --check -q src tests
	@flake8 src tests
	@mypy src tests

fix: ensure-fix-dependencies $(VERSION)
	@black src tests
	@isort src tests
