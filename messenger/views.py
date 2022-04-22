from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import managment
from .models import *
import random

@csrf_exempt
def messages(request):
    if request.user.is_authenticated:
        return render(request, "messages.html", {
            'messages': managment.load_mails(request)
        })
    else:
        return render(request, "404.html")

@csrf_exempt
def create_message(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            send_to = request.POST["send_to"]
            html = request.POST["html"]
            text = request.POST["text"]
            subject = request.POST["subject"]

            from_whom = request.user.username

            message_id = random.randint(0, 1 * (10 ** 7))

            if send_to == "" or subject == "":
                return render(request, "create-message.html", {
                    "error": "Try Again",
                })
            else:
                new = SentMail(
                    send_to=send_to,
                    from_whom=from_whom,
                    message=text, html=html,
                    subject=subject,
                    is_in_trash=False,
                    message_id=message_id
                )
                new.save()

            return render(request, "message-sent.html")
        else:
            return render(request, "create-message.html")
    else:
        return render(request, "404.html")

@csrf_exempt
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

@csrf_exempt
def trash(request):
    if request.user.is_authenticated:
        messages = SentMail.objects.filter(
            is_in_trash=True
        )
        return render(request, "trash.html", {
            "messages": messages
        })
    else:
        return render(request, "404.html")

@csrf_exempt
def delete_message(request, id, permanent_delete):
    if request.user.is_authenticated:
        if permanent_delete != 1:
            message_to_delete = SentMail.objects.get(
                message_id=id,
            )
            message_to_delete.is_in_trash = True
            message_to_delete.save()
            return redirect("/inbox")
        else:
            SentMail.objects.filter(message_id=id).delete()
            return redirect("/inbox/trash")
    else:
        return render(request, "404.html")
