import csv
from typing import Union

from django.conf import settings
from utils.data_types import FAKER
from ..models import Column, Schema


def generate_row(schema_columns: list[Column]) -> dict[Union[str, int]]:
    row = {}
    for column in schema_columns:
        col_type = column.get_type_display()
        if col_type == "Integer":
            start = column.start_integer
            end = column.end_integer
            data = FAKER.get(col_type)(start, end)
        elif col_type == "Text":
            sentences = column.sentences
            data = FAKER.get(col_type)(sentences)
        else:
            data = FAKER.get(col_type)()
        row[column.header] = data
    return row


def generate_csv(schema: Schema = Schema.objects.get(title="Test schema"), rows_quantity: int = 20):
    separator = schema.separator
    quotes = schema.quotes
    schema_columns: list[Column] = [column for column in schema.column.all()]
    # csv.register_dialect(
    #     delimiter=separator,
    #     quoting=quotes
    # )

    with open(settings.BASE_DIR / "test.csv", "w") as file:
        headers = [column.header for column in schema.column.all()]
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        for row in range(rows_quantity):
            writer.writerow(generate_row(schema_columns))
    """
        column_headers = list(data[0].keys())
    writer = csv.DictWriter(file, column_headers)
    writer.writeheader()
    [writer.writerow(item) for item in data]"""