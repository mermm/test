# Generated by Django 2.2.16 on 2020-09-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("glimpse", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="glimpse",
            name="content",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="glimpse",
            name="variant",
            field=models.CharField(
                blank=True,
                choices=[
                    (None, "Inherit"),
                    ("card_square", "Square card"),
                    ("row_half", "Half row"),
                    ("row_full", "Full row"),
                    ("quote", "Quote"),
                ],
                default=None,
                help_text="Form factor variant",
                max_length=50,
                null=True,
                verbose_name="Variant",
            ),
        ),
    ]
