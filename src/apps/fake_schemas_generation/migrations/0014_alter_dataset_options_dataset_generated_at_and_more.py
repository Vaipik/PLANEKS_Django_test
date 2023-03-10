# Generated by Django 4.1.7 on 2023-03-02 15:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("fake_schemas_generation", "0013_alter_dataset_csv_file"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dataset",
            options={
                "ordering": ["-generated_at", "is_uploaded", "id"],
                "verbose_name": "Dataset",
                "verbose_name_plural": "Datasets",
            },
        ),
        migrations.AddField(
            model_name="dataset",
            name="generated_at",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="dataset",
            name="is_uploaded",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="dataset",
            name="rows_quantity",
            field=models.PositiveSmallIntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name="dataset",
            table="generated_csvs",
        ),
    ]
