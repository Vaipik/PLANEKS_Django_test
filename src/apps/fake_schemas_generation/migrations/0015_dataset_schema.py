# Generated by Django 4.1.7 on 2023-03-02 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "fake_schemas_generation",
            "0014_alter_dataset_options_dataset_generated_at_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="dataset",
            name="schema",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dataset",
                to="fake_schemas_generation.schema",
            ),
            preserve_default=False,
        ),
    ]
