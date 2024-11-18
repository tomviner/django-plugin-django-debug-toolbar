default:
    @just --list

lint:
    ruff check
    ruff format --check

format:
    ruff format
    ruff check --fix --show-fixes --unsafe-fixes

check: lint test

test:
    pytest

install:
    pip install '.[test]'