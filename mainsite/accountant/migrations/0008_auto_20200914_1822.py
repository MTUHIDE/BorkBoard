# Generated by Django 3.1 on 2020-09-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0007_auto_20200914_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='last_email',
            field=models.DateTimeField(null=True),
        ),
    ]
