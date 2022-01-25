from django.shortcuts import render, redirect
import managment
from .models import *
import random


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

            message_id = random.randint(0, 1 * (10 ** 15))

            new = SentMail(send_to=send_to, from_whom=from_whom, message=text, html=html, subject=subject, is_in_trash=False, message_id=message_id)
            new.save()

            return render(request, "message-sent.html")
        else:
            return render(request, "create-message.html")
    else:
        return render(request, "404.html")


def view_message(request, id):
    if request.user.is_authenticated:
        message = SentMail.objects.get(
            message_id=id
        )
        return render(request, "message-display.html", {
            "message": message
        })
    else:
        return render(request, "404.html")
