# Generated by Django 4.0 on 2022-01-22 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_announcement'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ip',
        ),
    ]