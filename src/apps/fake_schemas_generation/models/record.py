from uuid import uuid4

from django.db import models

from utils.data_types import RECORD_DATA_TYPES
from ..libs import constants


class Record(models.Model):
    """DB Table for storing record data: header, data type, data"""
    id = models.UUIDField(
        default=uuid4,
        primary_key=True,
        editable=False
    )
    header = models.CharField(
        max_length=constants.COLUMN_HEADER_MAX_LENGTH,
        verbose_name="Column header"
    )
    type = models.CharField(
        max_length=constants.COLUMN_TYPE_LENGTH,
        choices=RECORD_DATA_TYPES,
        verbose_name="Record data type",
        default=""
    )
    data = models.TextField(
        verbose_name="Record data"
    )
    order = models.PositiveSmallIntegerField()
    schema = models.ForeignKey(
        to="fake_schemas_generation.Schema",
        on_delete=models.CASCADE,
        related_name="record"
    )

    class Meta:
        db_table = "schema_records"
        ordering = ["schema", "order"]
        verbose_name = "Record data"
        verbose_name_plural = "Records data"
        unique_together = ["header", "schema", "order"]

    def __str__(self) -> str:
        return f"{self.schema} | {self.header} | {self.get_type_display()} | {self.data[:30]}"
