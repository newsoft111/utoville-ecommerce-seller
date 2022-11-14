# Generated by Django 4.1.3 on 2022-11-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='productvariantvalue',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
