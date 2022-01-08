from django.db import models


class ip(models.Model):
    ip = models.CharField(max_length=16)
    location = models.CharField(max_length=100)
