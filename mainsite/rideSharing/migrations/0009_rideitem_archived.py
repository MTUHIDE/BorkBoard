# Generated by Django 2.2.5 on 2020-03-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rideSharing', '0008_auto_20200226_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='rideitem',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
