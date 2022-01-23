import socket
from app.models import *
from messenger.models import *

hostname = socket.gethostname()


def getIP():
    return socket.gethostbyname(hostname)


def validateIP(ipx):
    for i in blocked_ip.objects.all():
        if i.sus_ips == getIP():
            return False
    return True


def send_mail(send_to, request, html_message, message, subject):
    send_from = request.user.username
    new_message = SentMail(send_to=send_to, from_whom=send_from, message=message, html=html_message, subject=subject)
    new_message.save()


def load_mails(request):
    username = request.user.username
    mails = SentMail.objects.filter(
        send_to=username
    )
    return mails
