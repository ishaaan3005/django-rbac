# Generated by Django 4.2.3 on 2023-08-01 11:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rbac_app", "0015_rename_roles_api_mapped_users"),
    ]

    operations = [
        migrations.AlterField(
            model_name="api",
            name="mapped_users",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(null=True), size=None
            ),
        ),
    ]