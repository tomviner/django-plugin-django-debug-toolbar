# django-plugin-django-debug-toolbar

[![PyPI](https://img.shields.io/pypi/v/django-plugin-django-debug-toolbar.svg)](https://pypi.org/project/django-plugin-django-debug-toolbar/)
[![Changelog](https://img.shields.io/github/v/release/tomviner/django-plugin-django-debug-toolbar?include_prereleases&label=changelog)](https://github.com/tomviner/django-plugin-django-debug-toolbar/releases)
[![Tests](https://github.com/tomviner/django-plugin-django-debug-toolbar/workflows/Test/badge.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/tomviner/django-plugin-django-debug-toolbar/blob/main/LICENSE)

Django plugin that installs and configures the Django Debug Toolbar

## Goal

The Django Debug Toolbar is amazingly useful for development. It's so powerful that it's very dangerous to activate it in production.

The goal of this plugin is to enable a developer to activate the Django Debug Toolbar with the minimum number of steps, while keeping debug related code out of the codebase.

## Installation

First configure your Django project [to use DJP](https://djp.readthedocs.io/en/latest/installing_plugins.html).

Then install this plugin in the same environment as your Django application.
```bash
pip install django-plugin-django-debug-toolbar
```
## Usage

Looking at [Django Debug Toolbar's installation instructions](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html), this plugin takes care of the following steps (using their numbering):

- [#1. Install the Package](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install-the-package)
- [#3. Install the App](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#install-the-app)
- [#4. Add the URLs](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-urls)
- [#5. Add the Middleware](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#add-the-middleware)
- [#6. Configure Internal IPs](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips)
    - to include `127.0.0.1`

But you still need to:

- [#2. Check for Prerequisites](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#check-for-prerequisites)
    - like settings for static files and templates
- [#6. Configure Internal IPs](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#configure-internal-ips)
    - if you require IPs other than `127.0.0.1`, set them in `INTERNAL_IPS` in your settings
- [#7. Disable the toolbar when running tests (optional)](https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#disable-the-toolbar-when-running-tests-optional)
    - perhaps do this by disabling DJP when testing

## Middleware ordering

This plugin injects the Debug Toolbar Middleware early, but not too early, in the middleware list.

It needs to run after any midddleware that decodes requests (`GZipMiddleware`), or sets `request.META['REMOTE_ADDR']` (like [`django-xforwardedfor-middleware`](https://github.com/allo-/django-xforwardedfor-middleware) or [`django-xff`](https://github.com/ferrix/django-xff)).
If you have any other middleware that needs to run before the Debug Toolbar Middleware, please open a ticket and we'll add it to the `TOOLBAR_MUST_GO_AFTER` list.

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
