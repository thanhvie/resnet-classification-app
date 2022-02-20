pep8:
	flake8
run:
	python3 app.py

run-test:
	coverage run -m pytest
	coverage report