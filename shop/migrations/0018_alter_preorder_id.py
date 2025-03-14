# Generated by Django 5.0 on 2023-12-21 08:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0017_alter_announcement_image_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="preorder",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4,
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
