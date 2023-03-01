from uuid import uuid4

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth import get_user_model

from utils.data_types import STRING_QUOTES, COLUMN_SEPARATOR
from ..libs import constants


User = get_user_model()


class Schema(models.Model):
    """"""
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        max_length=constants.SCHEMA_TITLE_MAX_LENGTH,
        verbose_name="Schema title"
    )
    separator = models.CharField(
        max_length=constants.COLUMN_SEPARATOR_LENGTH,
        choices=COLUMN_SEPARATOR,
        default=",",
    )
    quotes = models.CharField(
        max_length=constants.COLUMN_STRING_QUOTES_LENGTH,
        choices=STRING_QUOTES,
        default='"',
    )
    slug = AutoSlugField(
        max_length=constants.SCHEMA_URL_MAX_LENGTH,
        populate_from="title",
        unique_with="user"
    )
    edited_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Edited"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="schema"
    )

    class Meta:
        db_table = "user_schemas"
        ordering = ["title", "-edited_at"]
        verbose_name = "Schema"
        verbose_name_plural = "Schemas"
        unique_together = ["title", "user"]

    def __str__(self) -> str:
        return f"{self.user} | {self.title}"
