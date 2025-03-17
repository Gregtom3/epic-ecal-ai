install:
	pip install --upgrade pip&&\
	pip install -r requirements.txt

format:
	black src/epic_ecal_ai/

lint:
	PYTHONPATH=src pylint --disable=R,C src/epic_ecal_ai/

test:
	MPLBACKEND=Agg PYTHONPATH=src pytest -v src/tests/*.py

all: install format lint test 