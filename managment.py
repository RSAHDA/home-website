import socket

# this is like this for now so that it can actually validate for now
hostname = socket.gethostname()
ips = [socket.gethostbyname(hostname)]


def getIP():
    return socket.gethostbyname(hostname)


def validateIP(ipx):
    for ip in ips:
        if ip == ipx:
            return True
        else:
            return False
