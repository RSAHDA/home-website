from django.db import models


class SentMail(models.Model):
    send_to = models.CharField(max_length=256)
    from_whom = models.CharField(max_length=256)
    message = models.TextField(max_length=999999999, blank=True)
    html = models.TextField(blank=True)
    subject = models.CharField(max_length=500)
