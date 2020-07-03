cov:
	open htmlcov/index.html

.PHONY: docs
docs:
	cd docs && \
	make html

fmt:
	poetry run isort -y
	poetry run black .

test:
	poetry run pytest
