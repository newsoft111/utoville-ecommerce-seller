# Generated by Django 4.1.3 on 2022-11-14 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
