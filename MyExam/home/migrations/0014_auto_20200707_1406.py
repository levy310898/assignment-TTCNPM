# Generated by Django 3.0.6 on 2020-07-07 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200707_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='dateCreate',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]