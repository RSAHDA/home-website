# Generated by Django 4.0 on 2022-03-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('url', models.CharField(max_length=2048)),
                ('description', models.CharField(max_length=2048)),
            ],
        ),
    ]