${VERSION}:
	@echo "__version__ = \"$(shell git describe --tag --always | grep -oE '[0-9]+\.[0-9]+\.[0-9]+' || echo "0.0.0")\"" > ${VERSION}
