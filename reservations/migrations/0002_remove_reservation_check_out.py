# Generated by Django 2.2.5 on 2021-03-11 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='check_out',
        ),
    ]
