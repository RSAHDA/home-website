from django.db import models


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)


class Announcement(models.Model):
    anouncement = models.TextField()


class UserJob(models.Model):
    username = models.CharField(max_length=999999)
    repo = models.CharField(max_length=999999, blank=True)
    job_title = models.CharField(max_length=999999)
