from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from ..models import Schema


User = get_user_model()


def create_schema(form_data):
    pass


def get_user_schemas(user: User) -> QuerySet[Schema]:
    """
    Return django queryset with user schemas
    :param user: user from request
    """
    return Schema.objects.filter(user=user)


def get_user_schema(user: User, schema_url: str) -> Schema:
    """

    :param user: user from request
    :param schema_url: sdssss
    """
    return Schema.objects.prefetch_related("row").get_object_or_404(slug=schema_url)
