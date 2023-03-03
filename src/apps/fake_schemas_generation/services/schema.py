from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from ..models import Schema


User = get_user_model()


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
    return Schema.objects.prefetch_related("column").get(user=user, slug=schema_url)
