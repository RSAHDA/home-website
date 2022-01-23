from django.db import models


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)


class Announcement(models.Model):
    anouncement = models.TextField()
