# Generated by Django 4.1.3 on 2022-11-14 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profit', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profit',
            name='is_done',
        ),
    ]
