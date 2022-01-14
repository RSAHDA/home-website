from django.db import models


class ip(models.Model):
    ip = models.CharField(max_length=16)
    location = models.CharField(max_length=100)


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)


class SentMail(models.Model):
    send_to = models.CharField(max_length=256)
    from_whom = models.CharField(max_length=256)
    message = models.TextField(max_length=999999999)
    html = models.TextField()
