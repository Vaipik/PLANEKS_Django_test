from uuid import uuid4

from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth import get_user_model

from ..libs import constants


User = get_user_model()


class Schema(models.Model):
    """"""
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False,
    )
    name = models.CharField(
        max_length=constants.SCHEMA_LENGTH_MAX_NAME,
        verbose_name="Schema name"
    )
    slug = AutoSlugField(
        max_length=constants.SCHEMA_URL_MAX_LENGTH,
        populate_from="name",
        unique_with="user"
    )
    rows_quantiy = models.PositiveIntegerField(
        verbose_name="Rows quantity"
    )
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="user"
    )

    class Meta:
        db_table = "user_schemas"
        ordering = ["name"]
        verbose_name = "Schema"
        verbose_name_plural = "Schemas"
        unique_together = ["name", "user"]

    def __str__(self) -> str:
        return f"{self.user} | {self.name}"
