# Generated by Django 4.1.3 on 2022-11-18 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_remove_product_name_product_product_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="productvariantvalue",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="productvariantvalue",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]