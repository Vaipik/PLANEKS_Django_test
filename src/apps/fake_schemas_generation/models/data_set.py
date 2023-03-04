from uuid import uuid4

from django.db import models

from utils.data_set import _get_folder_name


class DataSet(models.Model):
    """Is used to store generated datasets"""

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    csv_file = models.FileField(upload_to=_get_folder_name, editable=False)
    rows_quantity = models.IntegerField()
    generated_at = models.DateTimeField(
        auto_now_add=True
    )  # Date when DS has been created
    is_uploaded = models.BooleanField(default=False, editable=False)
    schema = models.ForeignKey(
        to="fake_schemas_generation.Schema",
        on_delete=models.CASCADE,
        related_name="dataset",
    )

    class Meta:
        db_table = "generated_csvs"
        verbose_name = "Dataset"
        verbose_name_plural = "Datasets"
        ordering = ["generated_at"]

    def __str__(self):
        return f"{self.schema} | {self.rows_quantity} {self.pk}"

    def delete(self, *args, **kwargs):
        self.csv_file.delete(save=False)  # Delete file directly from storage
        super().delete(*args, **kwargs)
