import csv
from typing import Union
from io import StringIO

from django.core.files.base import ContentFile
from django.db.models import QuerySet

from utils.data_types import FAKER
from ..models import Column, Schema, DataSet


def generate_row(schema_columns: list[Column]) -> list[Union[str, int]]:
    """
    Generating one row for csv with fake data
    :param schema_columns: list of schema columns
    :return: list with columns data
    """
    row = []
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
        row.append(data)
    return row


def generate_csv(dataset: DataSet):
    """This function is used to generate CSV in memory for EXISTED dataset
    and uploading generated csv. Afterwards updating dataset instance"""
    schema: Schema = dataset.schema
    separator = schema.separator
    quotes = schema.quotes
    schema_columns: list[Column] = [column for column in schema.column.all()]
    headers = [column.header for column in schema.column.all()]

    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer, delimiter=separator, quotechar=quotes)
    csv_writer.writerow(headers)
    for _ in range(dataset.rows_quantity):
        csv_writer.writerow(generate_row(schema_columns))

    csv_file = ContentFile(csv_buffer.getvalue().encode('utf-8'))

    dataset.csv_file.save("test.csv", csv_file)
    dataset.is_uploaded = True
    dataset.save()


def create_dataset(schema: Schema, rows_quantity: int) -> DataSet:
    ds = DataSet(schema=schema, rows_quantity=rows_quantity).save()
    return ds


def get_schema_datasets(schema: Schema) -> QuerySet[DataSet]:
    return DataSet.objects.filter(schema=schema)


def get_dataset(dataset_id) -> DataSet:
    return DataSet.objects.select_related("schema").get(pk=dataset_id)
