# Generated by Django 2.2.5 on 2020-04-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_catalogitem_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalogitem',
            name='item_description',
            field=models.CharField(blank=True, max_length=1500),
        ),
    ]
