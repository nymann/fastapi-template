CI_REGISTRY_IMAGE?=registry.nymann.dev/nymann/fastapi_template
ONBUILD?=${CI_REGISTRY_IMAGE}:onbuild

docker-build-onbuild-ci: ${VERSION} requirements.install
	@docker build -f docker/Dockerfile .

docker-push-onbuild-ci: ${VERSION} requirements.install
	@docker build \
		--cache-from ${ONBUILD} \
		-t ${ONBUILD} \
		-f docker/Dockerfile .
	@docker push ${CI_REGISTRY_IMAGE}

version-requirements: ${VERSION} requirements.install
	# This is used as a precursor to building images via the pipeline
	@echo "${VERSION}"

.PHONY:docker-build-onbuild-ci docker-push-onbuild-ci version-requirements
