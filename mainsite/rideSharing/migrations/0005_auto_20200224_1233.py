# Generated by Django 2.2.9 on 2020-02-24 17:33

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('rideSharing', '0004_auto_20200219_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='RideCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
            ],
        )

    ]
