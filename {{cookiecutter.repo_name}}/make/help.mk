help:
	@printf "\e[92m%s\e[0m\n" "make install"
	@echo " - Installs ${COMPONENT}."
	@printf "\e[92m%s\e[0m\n" "make install-all"
	@echo " - Install ${COMPONENT}, all development and tests dependencies."
	@printf "\e[92m%s\e[0m\n" "make test"
	@echo " - Runs integration tests and unit tests"
	@printf "\e[92m%s\e[0m\n" "make unit-test"
	@echo " - Runs integration tests"
	@printf "\e[92m%s\e[0m\n" "make integration-tests"
	@echo " - Runs unit tests"
	@printf "\e[92m%s\e[0m\n" "make lint"
	@echo " - Lints your code (black, flake8 and mypy)."
	@printf "\e[92m%s\e[0m\n" "make fix"
	@echo " - Autofixes imports and some formatting."

.PHONY: help
.DEFAULT: help
