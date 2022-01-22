import socket

from app.models import *

hostname = socket.gethostname()


def getIP():
    return socket.gethostbyname(hostname)


def validateIP(ipx):
    for i in blocked_ip.objects.all():
        if i.sus_ips == getIP():
            return False
    return True

# work on this chuck ragav, make it so that it adds messages to SentMail object.


def send_mail(send_to, request, html_message, message):
    pass
