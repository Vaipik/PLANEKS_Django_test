from uuid import uuid4

from django.db import models

from utils.data_types import ROW_DATA_TYPES
from ..libs import constants


class Row(models.Model):
    """DB Table for storing row data. Row header, row data type, row data"""
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False
    )
    header = models.CharField(
        max_length=constants.ROW_HEADER_MAX_LENGTH,
        verbose_name="Row header"
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
        related_name="row"
    )

    class Meta:
        db_table = "schema_rows"
        ordering = ["schema", "type"]
        verbose_name = "Row data"
        verbose_name_plural = "Rows data"
        unique_together = ["header", "schema"]

    def __str__(self) -> str:
        return f"{self.schema} | {self.header} | {self.get_type_display()} | {self.data[:30]}"
