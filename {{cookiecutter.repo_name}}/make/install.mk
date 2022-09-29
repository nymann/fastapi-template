install: ${VERSION}
	@pip install .

install-all: ${VERSION}
	@pip install -e '.[all]'

install-dev: ${VERSION}
	@pip install -e '.[dev]'

install-tests: ${VERSION}
	@pip install -e '.[tests]'

install-package: ${VERSION}
	@pip install '.[package]'
