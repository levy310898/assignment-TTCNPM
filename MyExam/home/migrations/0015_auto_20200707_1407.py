# Generated by Django 3.0.6 on 2020-07-07 07:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20200707_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='dateCreate',
            field=models.DateField(blank=True, default=datetime.datetime.now, editable=False),
        ),
    ]