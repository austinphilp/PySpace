install: 
	venv/bin/pip3 install --upgrade -r requirements.txt
	venv/bin/pip3 install -e .

serve: 
	venv/bin/python3 space/server.py

venv:
	pip3 install --user virtualenv
	python3 -m virtualenv venv

test:
	make venv
	venv/bin/python3 -m pytest space/tests

flake8:
	venv/bin/flake8 space/
