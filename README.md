# django-plugin-django-debug-toolbar

[![PyPI](https://img.shields.io/pypi/v/django-plugin-django-debug-toolbar.svg)](https://pypi.org/project/django-plugin-django-debug-toolbar/)
[![Changelog](https://img.shields.io/github/v/release/tomviner/django-plugin-django-debug-toolbar?include_prereleases&label=changelog)](https://github.com/tomviner/django-plugin-django-debug-toolbar/releases)
[![Tests](https://github.com/tomviner/django-plugin-django-debug-toolbar/workflows/Test/badge.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/blob/main/LICENSE)

Django plugin that configures the Django Debug Toolbar

## Installation

First configure your Django project [to use DJP](https://djp.readthedocs.io/en/latest/installing_plugins.html).

Then install this plugin in the same environment as your Django application.
```bash
pip install django-plugin-django-debug-toolbar
```
## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd django-plugin-django-debug-toolbar
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
