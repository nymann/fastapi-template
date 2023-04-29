package: ${VERSION} setup.py
	@python setup.py sdist bdist_wheel

.PHONY:package
