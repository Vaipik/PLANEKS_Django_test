from django.apps import AppConfig


class FakeSchemasGenerationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_schemas_generation'
