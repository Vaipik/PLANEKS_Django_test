# Generated by Django 4.1.7 on 2023-03-02 11:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fake_schemas_generation", "0008_alter_schema_options"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="record",
            unique_together={("schema", "order", "header")},
        ),
    ]
