cov:
	open htmlcov/index.html

.PHONY: docs
docs:
	poetry export --dev -f requirements.txt > docs/requirements.txt
	cd docs && \
	make html

fmt:
	poetry run isort -y
	poetry run black .

setup:
	asdf install
	poetry install

test:
	poetry run pytest
