help:
	@printf "\e[92m%s\e[0m\n" "make install"
	@echo " - Installs dependencies and ${COMPONENT}."
	@printf "\e[92m%s\e[0m\n" "make hooks"
	@echo " - Setup pre-commit hooks"
	@printf "\e[92m%s\e[0m\n" "make test"
	@echo " - Run tests"
	@printf "\e[92m%s\e[0m\n" "make format"
	@echo " - Autoformats code and sorts imports."
	@printf "\e[92m%s\e[0m\n" "make lint"
	@echo " - Lints your code."
	@printf "\e[92m%s\e[0m\n" "make run"
	@echo " - Runs ${COMPONENT}"

.PHONY: help
.DEFAULT: help
