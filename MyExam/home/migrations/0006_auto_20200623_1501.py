# Generated by Django 3.0.7 on 2020-06-23 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200623_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='birthDate',
            field=models.DateField(),
        ),
    ]
