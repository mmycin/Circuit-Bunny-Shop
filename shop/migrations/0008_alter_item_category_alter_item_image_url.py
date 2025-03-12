# Generated by Django 5.0 on 2023-12-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0007_alter_item_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="Category",
            field=models.CharField(default="", max_length=100),
        ),
        migrations.AlterField(
            model_name="item",
            name="Image_URL",
            field=models.URLField(default=""),
        ),
    ]
