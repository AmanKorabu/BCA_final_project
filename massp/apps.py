from django.apps import AppConfig


class CoatingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'massp'

    def ready (self):
        import massp.signals