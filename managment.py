import socket

import app.models
from app.models import *

# this is like this for now so that it can actually validate for now.

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

