setup:
	python -m venv environments/venv && . environments/venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.dev
	pip install -r requirements.prod

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -f .coverage.*

clean: clean-pyc clean-test

test: clean
	. environments/venv/bin/activate && py.test tests --cov=src --cov-report=term-missing --cov-fail-under 10

mypy:
	. environments/venv/bin/activate && mypy src

lint:
	. environments/venv/bin/activate && pylint src -j 4 --reports=y

docs: FORCE
	cd docs; . environments/venv/bin/activate && sphinx-apidoc -o ./source ./src
	cd docs; . environments/venv/bin/activate && sphinx-build -b html ./source ./build
FORCE:

check: test lint mypy

train: python train_pipeline.py