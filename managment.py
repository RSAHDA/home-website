import socket
from app.models import *

# this is like this for now so that it can actually validate for now.

hostname = socket.gethostname()
ips = ip.objects.all()


def getIP():
    return socket.gethostbyname(hostname)


def validateIP(ipx):
    for ip in ips:
        if ip.ip == ipx:
            return True
        else:
            return False

