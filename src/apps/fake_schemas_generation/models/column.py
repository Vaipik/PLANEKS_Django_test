from uuid import uuid4

from django.db import models

from utils.data_types import RECORD_DATA_TYPES
from ..libs import constants


class Column(models.Model):
    """DB Table for storing column data: header, data type, data"""

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    header = models.CharField(
        max_length=constants.COLUMN_HEADER_MAX_LENGTH, verbose_name="Column header"
    )
    start_integer = models.PositiveSmallIntegerField(
        default=None, blank=True, null=True
    )
    end_integer = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    sentences = models.PositiveSmallIntegerField(default=None, blank=True, null=True)
    type = models.CharField(
        max_length=constants.COLUMN_TYPE_LENGTH,
        choices=RECORD_DATA_TYPES,
        verbose_name="Column data type",
        default="",
    )
    order = models.PositiveSmallIntegerField()
    schema = models.ForeignKey(
        to="fake_schemas_generation.Schema",
        on_delete=models.CASCADE,
        related_name="column",
    )

    class Meta:
        db_table = "schema_columns"
        ordering = ["schema", "order"]
        verbose_name = "Record data"
        verbose_name_plural = "Records data"
        unique_together = ["schema", "order"]

    def __str__(self) -> str:
        return f"{self.schema} | {self.header} | {self.get_type_display()} | {self.data[:30]}"
