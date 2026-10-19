.PHONY: setup test build

setup:
	python3 -m pip install -e ".[dev]"

test:
	python3 -m pytest

build:
	python3 -m pip wheel --no-deps -w dist .
