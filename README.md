# django-plugin-django-debug-toolbar

[![PyPI](https://img.shields.io/pypi/v/django-plugin-django-debug-toolbar.svg)](https://pypi.org/project/django-plugin-django-debug-toolbar/)
[![Changelog](https://img.shields.io/github/v/release/tomviner/django-plugin-django-debug-toolbar?include_prereleases&label=changelog)](https://github.com/tomviner/django-plugin-django-debug-toolbar/releases)
[![Tests](https://github.com/tomviner/django-plugin-django-debug-toolbar/workflows/Test/badge.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/blob/main/LICENSE)

Django plugin that installs and configures the Django Debug Toolbar

## Installation

First configure your Django project [to use DJP](https://djp.readthedocs.io/en/latest/installing_plugins.html).

Then install this plugin in the same environment as your Django application.
```bash
pip install django-plugin-django-debug-toolbar
```
## Usage

Looking at [Django Debug Toolbar's installation instructions](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html) - *and using their numbering* - this plugin takes care of the following steps:

- 1. Install the Package
- 3. Install the App
- 4. Add the URLs
- 5. Add the Middleware
- 6. Configure Internal IPs

But you still need to:

- 2. Check for Prerequisites
    - like settings for static files and templates
- 6. Configure Internal IPs
    - if you require IPs other than 127.0.0.1, set them in `INTERNAL_IPS` in your settings
- 7. Disable the toolbar when running tests (optional)
    - perhaps do this by disabling djp when testing

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
