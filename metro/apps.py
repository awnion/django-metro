from django.apps import AppConfig
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class MetroConfig(AppConfig):
    name = "metro"
    default_auto_field = "django.db.models.AutoField"
    verbose_name = getattr(settings, "METRO_APP_TITLE", _("Metro"))
