PYTHON := python

.PHONY: format lint test ci

format:
	$(PYTHON) -m black .
	$(PYTHON) -m ruff check . --fix

lint:
	$(PYTHON) -m ruff check .
	$(PYTHON) -m black --check .
	$(PYTHON) -m mypy src

test:
	pytest -q --junitxml=test-results/junit.xml --cov=app --cov-report=xml:coverage.xml

ci: lint test
