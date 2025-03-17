install:
	pip install --upgrade pip&&\
	pip install -r requirements.txt

format:
	black src/epic-ecal-ai/*.py

lint:
	pylint --disable=R,C src/epic_ecal_ai/*.py

test:
	PYTHONPATH=src pytest -v src/tests/*.py

all: install format lint test 