# Generated by Django 4.1.7 on 2023-03-02 14:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("fake_schemas_generation", "0011_column_delete_record"),
    ]

    operations = [
        migrations.CreateModel(
            name="DataSet",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("csv_file", models.FileField(upload_to="csvs")),
            ],
        ),
    ]
