import djp
from debug_toolbar.toolbar import debug_toolbar_urls


@djp.hookimpl
def installed_apps():
    return ["debug_toolbar"]


@djp.hookimpl
def urlpatterns():
    return debug_toolbar_urls()


@djp.hookimpl
def settings(current_settings):
    current_settings.setdefault("INTERNAL_IPS", []).append("127.0.0.1")

    # Debug Toolbar will only display when DEBUG = True
    current_settings["DEBUG"] = True

    current_settings["MIDDLEWARE"] = inject_middleware(current_settings["MIDDLEWARE"])


def next_index_or_start(list, item):
    try:
        return list.index(item) + 1
    except ValueError:
        return 0


def inject_middleware(current_middleware):
    """Inject DebugToolbarMiddleware early, but not too early."""
    TOOLBAR_MUST_GO_AFTER = [
        "django.middleware.gzip.GZipMiddleware",
        "xff.middleware.XForwardedForMiddleware",
        "x_forwarded_for.middleware.XForwardedForMiddleware",
    ]
    position = max(
        next_index_or_start(current_middleware, mw) for mw in TOOLBAR_MUST_GO_AFTER
    )

    return [
        *current_middleware[:position],
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        *current_middleware[position:],
    ]
