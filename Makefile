install: 
	venv/bin/pip3 install -r requirements.txt
	venv/bin/pip3 install -e .

venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

test:
	make venv
	venv/bin/python3 -m pytest space/*

flake8:
	venv/bin/flake8