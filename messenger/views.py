from django.shortcuts import render, redirect
import managment
from .models import *


def messages(request):
    if request.user.is_authenticated:
        return render(request, "messages.html", {
            'messages': managment.load_mails(request)
        })
    else:
        return render(request, "404.html")


def create_message(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            send_to = request.POST["send_to"]
            html = request.POST["html"]
            text = request.POST["text"]
            subject = request.POST["subject"]

            from_whom = request.user.username

            new = SentMail(send_to=send_to, from_whom=from_whom, message=text, html=html, subject=subject)
            new.save()
            return render(request, "message-sent.html")
        else:
            return render(request, "create-message.html")
    else:
        return render(request, "404.html")
