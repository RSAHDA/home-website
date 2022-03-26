# Generated by Django 4.0 on 2022-03-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_delete_userjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, unique=True)),
                ('username', models.CharField(max_length=999999)),
                ('repo', models.CharField(blank=True, max_length=999999)),
                ('job_title', models.CharField(max_length=999999, unique=True)),
            ],
        ),
    ]