# Generated by Django 3.1.3 on 2020-11-17 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("courses", "0018_auto_20201102_1912"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursepluginmodel",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("glimpse", "Default"),
                    ("glimpse", "Small"),
                    ("glimpse__large", "Large"),
                ],
                help_text="Optional glimpse variant for a custom look.",
                max_length=50,
                null=True,
                verbose_name="variant",
            ),
        ),
    ]
