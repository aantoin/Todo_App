from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ChecklistsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo_app.checklists"
    verbose_name = _("Checklists")
