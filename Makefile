cov:
	open htmlcov/index.html

.PHONY: docs
docs:
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
