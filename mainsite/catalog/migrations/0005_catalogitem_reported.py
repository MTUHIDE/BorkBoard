# Generated by Django 3.1 on 2020-09-11 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200827_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogitem',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
