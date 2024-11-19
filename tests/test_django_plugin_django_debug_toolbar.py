import pytest
from django.conf import settings
from django.test.client import Client

from django_plugin_django_debug_toolbar import inject_middleware


def test_simple_view_works():
    response = Client().get("/")
    assert response.status_code == 200
    assert response.content == b"Hello world"


def test_installed_apps_injected():
    assert "debug_toolbar" in settings.INSTALLED_APPS


def test_urlpatterns_injected():
    urlconf = __import__(settings.ROOT_URLCONF)
    assert len(urlconf.test_project.urls.urlpatterns) > 1


def test_internal_ips_injected():
    assert "127.0.0.1" in settings.INTERNAL_IPS


def test_debug_is_true():
    assert settings.DEBUG is True


def test_toolbar_middleware_injected():
    assert settings.MIDDLEWARE == [
        "django.middleware.locale.LocaleMiddleware",
        "django.middleware.gzip.GZipMiddleware",
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        "django.middleware.security.SecurityMiddleware",
    ]


def test_debug_toolbar_panel_page_served():
    response = Client(raise_request_exception=False).get("/__debug__/render_panel/")
    assert response.status_code != 404


@pytest.mark.parametrize(
    "middleware, expected_middleware",
    [
        ([], ["debug_toolbar.middleware.DebugToolbarMiddleware"]),
        (["a", "b"], ["debug_toolbar.middleware.DebugToolbarMiddleware", "a", "b"]),
        (
            ["django.middleware.gzip.GZipMiddleware"],
            [
                "django.middleware.gzip.GZipMiddleware",
                "debug_toolbar.middleware.DebugToolbarMiddleware",
            ],
        ),
        (
            ["a", "django.middleware.gzip.GZipMiddleware"],
            [
                "a",
                "django.middleware.gzip.GZipMiddleware",
                "debug_toolbar.middleware.DebugToolbarMiddleware",
            ],
        ),
        (
            ["a", "django.middleware.gzip.GZipMiddleware", "b"],
            [
                "a",
                "django.middleware.gzip.GZipMiddleware",
                "debug_toolbar.middleware.DebugToolbarMiddleware",
                "b",
            ],
        ),
        (
            [
                "a",
                "django.middleware.gzip.GZipMiddleware",
                "b",
                "x_forwarded_for.middleware.XForwardedForMiddleware",
                "d",
            ],
            [
                "a",
                "django.middleware.gzip.GZipMiddleware",
                "b",
                "x_forwarded_for.middleware.XForwardedForMiddleware",
                "debug_toolbar.middleware.DebugToolbarMiddleware",
                "d",
            ],
        ),
        (
            [
                "a",
                "x_forwarded_for.middleware.XForwardedForMiddleware",
                "b",
                "django.middleware.gzip.GZipMiddleware",
                "xff.middleware.XForwardedForMiddleware",
                "d",
            ],
            [
                "a",
                "x_forwarded_for.middleware.XForwardedForMiddleware",
                "b",
                "django.middleware.gzip.GZipMiddleware",
                "xff.middleware.XForwardedForMiddleware",
                "debug_toolbar.middleware.DebugToolbarMiddleware",
                "d",
            ],
        ),
    ],
)
def test_toolbar_middleware_injected_order(middleware, expected_middleware):
    assert inject_middleware(middleware) == expected_middleware
