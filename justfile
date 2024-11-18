default:
    @just --list

lint:
    ruff check
    ruff format --check
    typos

format:
    ruff format
    ruff check --fix --show-fixes --unsafe-fixes
    typos --write-changes

check: lint test

test:
    pytest

install:
    pip install '.[test]'