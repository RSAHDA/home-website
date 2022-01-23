from django.db import models


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)


class SentMail(models.Model):

    send_to = models.CharField(max_length=256)
    from_whom = models.CharField(max_length=256)
    message = models.TextField(max_length=999999999)
    html = models.TextField()


class Announcement(models.Model):
    anouncement = models.TextField()
