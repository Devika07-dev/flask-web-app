setup:
	python3 -m venv venv
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv

lint:
	pylint --disable=R,C app.py

run:
	python app.py
