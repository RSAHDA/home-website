# Generated by Django 4.0.3 on 2022-03-26 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_userjob'),
    ]

    operations = [
        migrations.DeleteModel(
            name='blocked_ip',
        ),
        migrations.DeleteModel(
            name='UserJob',
        ),
    ]