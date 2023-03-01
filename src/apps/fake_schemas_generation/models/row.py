from uuid import uuid4

from django.db import models

from utils.data_types import ROW_DATA_TYPES
from ..libs import constants


class Row(models.Model):
    """"""
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False
    )
    type = models.CharField(
        max_length=constants.ROW_TYPE_LENGTH,
        choices=ROW_DATA_TYPES,
        verbose_name="Row data type"
    )
    data = models.TextField(
        verbose_name="Row data"
    )
    schema = models.ForeignKey(
        to="fake_schemas_generation.Schema",
        on_delete=models.CASCADE,
        related_name="schema"
    )

    class Meta:
        db_table = "schema_rows"
        ordering = ["schema", "type"]
        verbose_name = "Row data"
        verbose_name_plural = "Rows data"

    def __str__(self) -> str:
        return f"{self.schema} | {self.get_type_display()} | {self.data[:30]}"

