# Generated by Django 3.0.7 on 2020-06-23 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200623_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='info',
            name='lastName',
        ),
    ]