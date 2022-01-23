from django.db import models


class ip(models.Model):
    ip = models.CharField(max_length=16)
    location = models.CharField(max_length=100)


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)



