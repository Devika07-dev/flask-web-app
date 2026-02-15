all: setup install lint test run

setup:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

install:
	pip install --upgrade pip && pip install -r requirements.txt

lint:
	pylint --disable=R,C app.py

test:
	python -m pytest -vv

run:
	python app.py
