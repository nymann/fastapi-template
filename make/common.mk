hooks:${TMP_HOOKS}
${TMP_HOOKS}:.pre-commit-config.yaml
	@pip install pre-commit > /dev/null
	@pre-commit install > /dev/null
	@pre-commit run --all-files || \
		(printf "\e[93m%s\e[0m\n" "Run same make target again";exit 1)
	@printf "\e[92m%s\e[0m\n" "Pre-commit hooks ran successfully"
	@touch /tmp/.${COMPONENT}_hooks.empty_target

requirements.install: setup.cfg ${SCRIPTS_DIR}/requirements_parser.py
	${SCRIPTS_DIR}/requirements_parser.py install > requirements.install

requirements.test: setup.cfg ${SCRIPTS_DIR}/requirements_parser.py
	${SCRIPTS_DIR}/requirements_parser.py test > requirements.test

${VERSION}:
	#@echo "__version__ = \"$(shell git describe --tag --always | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')\"" > ${VERSION}
	@echo "__version__ = \"$(shell git describe --tag --always)\"" > ${VERSION}
