# Generated by Django 3.0.7 on 2020-07-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20200707_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]