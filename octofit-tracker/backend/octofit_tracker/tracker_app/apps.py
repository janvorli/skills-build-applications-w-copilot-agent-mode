from django.apps import AppConfig


class TrackerAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "octofit_tracker.tracker_app"

    def ready(self):
        pass
