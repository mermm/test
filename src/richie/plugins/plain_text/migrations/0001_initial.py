# Generated by Django 2.1.5 on 2019-02-09 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("cms", "0022_auto_20180620_1551")]

    operations = [
        migrations.CreateModel(
            name="PlainText",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="plain_text_plaintext",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("body", models.TextField(verbose_name="plain text")),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        )
    ]
