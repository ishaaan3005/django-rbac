# Generated by Django 4.2.3 on 2023-07-30 19:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rbac_app", "0012_alter_api_roles"),
    ]

    operations = [
        migrations.AlterField(
            model_name="api",
            name="roles",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(blank=True, max_length=100, null=True),
                size=None,
            ),
        ),
    ]
