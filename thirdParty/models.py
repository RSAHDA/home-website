from django.db import models


class Id(models.Model):
    application_host = models.CharField(max_length=2048)
    application_id = models.CharField(max_length=2048)
