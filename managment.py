import socket

from app.models import *
from django.contrib.auth.models import User

hostname = socket.gethostname()
ips = ip.objects.all()


def getIP():
    return socket.gethostbyname(hostname)


def validateIP(ipx):
    for i in blocked_ip.objects.all():
        if i.sus_ips == getIP():
            return False

    for ip in ips:
        if ip.ip == ipx:
            return True
        else:
            return False

def send_mail(send_to, request, html_message, message):
    pass
