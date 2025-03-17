install:
	pip install --upgrade pip&&\
	pip install -r requirements.txt

format:
	black src/epic-ecal-ai/*.py

lint:
	pylint --disable=R,C src/epic-ecal-ai/*.py

all: install format lint