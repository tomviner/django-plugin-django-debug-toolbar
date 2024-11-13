import djp
from debug_toolbar.toolbar import debug_toolbar_urls


@djp.hookimpl
def installed_apps():
    # A list of app strings to add to INSTALLED_APPS:
    return ["debug_toolbar"]


@djp.hookimpl
def urlpatterns():
    # A list of URL patterns to add to urlpatterns:
    return debug_toolbar_urls()


@djp.hookimpl
def settings(current_settings):
    # Make changes to the Django settings.py globals here
    INTERNAL_IPS = current_settings.get("INTERNAL_IPS", [])
    INTERNAL_IPS.append("127.0.0.1")
    current_settings["INTERNAL_IPS"] = INTERNAL_IPS

    # Debug Toolbar will only display when DEBUG = True
    current_settings["DEBUG"] = True



@djp.hookimpl
def middleware():
    # A list of middleware class strings to add to MIDDLEWARE:
    # Wrap strings in djp.Before("middleware_class_name") or
    # djp.After("middleware_class_name") to specify before or after
    return [
        djp.Before("debug_toolbar.middleware.DebugToolbarMiddleware")
    ]
