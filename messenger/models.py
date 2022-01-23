from django.db import models


class SentMail(models.Model):
    send_to = models.CharField(max_length=256)
    from_whom = models.CharField(max_length=256)
    message = models.TextField(max_length=999999999)
    html = models.TextField()
