from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=2048)
    url = models.CharField(max_length=2048)
    description = models.CharField(max_length=2048)
