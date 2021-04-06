lint: install-local
	pip install pylint isort
	pylint --rcfile=setup.cfg -r n src > pylint.txt
	isort --recursive --diff src
