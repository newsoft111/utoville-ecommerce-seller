# Generated by Django 4.1.3 on 2022-11-11 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('revenue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='revenueseller',
            old_name='refunt_amount',
            new_name='refund_amount',
        ),
    ]