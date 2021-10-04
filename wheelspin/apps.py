from django.apps import AppConfig


class WheelspinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wheelspin'

    def ready(self):
        import wheelspin.signals
