# Generated by Django 2.2.5 on 2021-03-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_remove_reservation_check_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='check_out',
            field=models.DateField(null=True),
        ),
    ]