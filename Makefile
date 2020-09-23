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

build:
	poetry build

clean:
	rm -rf dist

publish: clean build
	poetry publish

release: clean build
	ghr -u crflynn -r stochastic -c $(shell git rev-parse HEAD) -delete -b "release" -n $(shell poetry version | tail -c +12) $(shell poetry version | tail -c +12) dist/
